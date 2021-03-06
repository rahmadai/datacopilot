from pytorch_lightning import Trainer
from argparse import Namespace

from torchnlp.encoders.text import CharacterEncoder, WhitespaceEncoder

# related to pretrained tokenizer & model
from transformers import ElectraModel, ElectraTokenizer
from kobert_transformers import get_kobert_model, get_distilkobert_model
from kobert_transformers import get_tokenizer as kobert_tokenizer
from transformers import BertForMaskedLM

from .DIET_lightning_model import DualIntentEntityTransformer
from .dataset.intent_entity_dataset import RasaIntentEntityDataset

import os, sys
import torch
from torch.utils.data import DataLoader
from DIET.eval import PerfCallback


def train(
    file_path,
    # training args
    train_ratio=0.8,
    batch_size=None,
    optimizer="Adam",
    intent_optimizer_lr=1e-5,
    entity_optimizer_lr=2e-5,
    checkpoint_path=os.getcwd(),
    max_epochs=20,
    tokenizer_type="bert",
    # model args
    # refered below link to optimize model
    # https://www.notion.so/A-Primer-in-BERTology-What-we-know-about-how-BERT-works-aca45feaba2747f09f1a3cdd1b1bbe16
    backbone="bert",
    d_model=256,
    num_encoder_layers=2,
    **kwargs
):
    gpu_num = torch.cuda.device_count()

    if backbone is None:
        report_nm = "diet_{}_tokenizer_report.json".format(tokenizer_type)
    else:
        report_nm = "{}_report.json".format(backbone)

    if batch_size is not None:
        trainer = Trainer(
            default_root_dir=checkpoint_path,
            max_epochs=max_epochs,
            gpus=gpu_num,
            callbacks=[
                PerfCallback(
                    gpu_num=gpu_num, report_nm=report_nm, root_path=checkpoint_path
                )
            ],
        )
    else:
        trainer = Trainer(
            default_root_dir=checkpoint_path,
            max_epochs=max_epochs,
            gpus=gpu_num,
            auto_scale_batch_size="binsearch",
            callbacks=[
                PerfCallback(
                    gpu_num=gpu_num, report_nm=report_nm, root_path=checkpoint_path
                )
            ],
        )

    model_args = {}

    # training args
    model_args["max_epochs"] = max_epochs
    model_args["nlu_data"] = open(file_path, encoding="utf-8").readlines()
    model_args["train_ratio"] = train_ratio
    model_args["batch_size"] = batch_size
    model_args["optimizer"] = optimizer
    model_args["intent_optimizer_lr"] = intent_optimizer_lr
    model_args["entity_optimizer_lr"] = entity_optimizer_lr

    if backbone is None:
        model_args["tokenizer"] = tokenizer_type

    else:
        if backbone in ["kobert", "distill_kobert"]:
            model_args["tokenizer"] = "kobert"
        elif backbone == "koelectra":
            model_args["tokenizer"] = ElectraTokenizer.from_pretrained(
                "monologg/koelectra-small-v2-discriminator"
            )
        elif backbone == "bert":
            model_args["tokenizer"] = "bert"
        elif backbone == "indobert":
            model_args["tokenizer"] = "indobert"
        elif backbone == "indodistilbert":
            model_args["tokenizer"] = "indodistilbert"

    # model args
    model_args["backbone"] = backbone
    model_args["d_model"] = d_model
    model_args["num_encoder_layers"] = num_encoder_layers

    for key, value in kwargs.items():
        model_args[key] = value

    hparams = Namespace(**model_args)

    model = DualIntentEntityTransformer(hparams)

    trainer.fit(model)
