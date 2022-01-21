from DIET import trainer
import os


def main():
    trainer.train(
        "dataset/rasa_format/copilot_dataset_01.yaml",
        train_ratio=0.8,
        batch_size=32,
        optimizer="Adam",
        intent_optimizer_lr=1e-5,
        entity_optimizer_lr=2e-5,
        checkpoint_path=os.getcwd(),
        max_epochs=10,
        num_encoder_layers=3,
        tokenizer_type="bert",
        backbone="bert",
    )


if __name__ == "__main__":
    main()
