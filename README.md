

<br />
<h1>
<p align="center">
  <img src="logo/datacopilot.jpg" alt="Logo" height=200>
  <br>Data Copilot
</h1>
  <p align="center">
    <br />
    </p>
</p>

<p align="center">
<a href="https://www.python.org/"><img alt="Actions Status" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## 🎯 What is Data Copilot ?
Data Copilot is AI assistant for data scientist and data analyst for suggest snippets of codes using implementation of Intent and Entity classifier. Data Copilot use DIET for classify user requests (intent and entity) and provide text output in the form of code suggestions. DIET its have means **Dual Intent and Entity Transformer** so the model can predict the intent and entity simultaneously from the input of text. 

## 🚀 How to Use

**Inference using Google Colab :**  <a href="https://colab.research.google.com/drive/1t6tFvnmv0ZABuCio_xweogg_wx3bMrAx#scrollTo=cx3DwG43cJDz"><img alt="Actions Status" src="https://colab.research.google.com/assets/colab-badge.svg"></a> </br>

**1. Clone our repository**

```bash
% git clone https://github.com/rahmadai/githubcopilot.git
```

**2. Install requirements**

```bash
% cd datacopilot
% pip install -r requirements.txt
```

**3. Download model**

```bash
%  wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1QstKji0PimR9w0TJ_0HR1E9xcTSs9lJ7' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1QstKji0PimR9w0TJ_0HR1E9xcTSs9lJ7" -O epoch9.ckpt && rm -rf /tmp/cookies.txt

```

**4. Inference**
</br>Example code for inference
```bash
import sys
import pprint

sys.path.append("datacopilot")
from DIET import Inferencer
from DIET.postprocessing import post_processing

inferencer = Inferencer(
        "model/checkpoints/epoch=9.ckpt"
    )

text = "put the latest dataset.csv on gdrive using pandas into my program"
result = post_processing(inferencer.inference(text, intent_topk=1))
pprint.pprint(result)
```
Output
```bash
{'entities': [{'end': 19,
               'entity': 'datasate_name',
               'start': 15,
               'value': 'dataset.csv'},
              {'end': 31,
               'entity': 'directory',
               'start': 30,
               'value': 'gdrive'},
              {'end': 48,
               'entity': 'lib_name',
               'start': 43,
               'value': 'pandas'}],
 'intent': {'confidence': 0.9954274892807007, 'name': 'dataset/load'},
 'intent_ranking': [{'confidence': 0.9954274892807007, 'name': 'dataset/load'}],
 'text': 'put the latest dataset.csv on gdrive using pandas into my program'}
 ```


## 📊 Model Performance
Here is the model performance by fine tuning it using BERT pretrained model and custom dataset. Evalution metrics is calculated use weighted avg.
| Model              |       Task             | F1-Score      | Recall        |   Precision      |
| ------------------ | -----------------------|:-------------:|:-------------:|:----------------:|
| Data-Copilot-0.0.1 | Intent                 | 89.37         |    89.39      |    89.54         |
| Data-Copilot-0.0.1 | Entity                 | 87.78         |    81.83      |    94.65         |

## 📄 License
MIT License
<br>
Pull Request are open
<br>
Written by Rahmad Kurniawan, 2022

Many thanks to Ilham Fazri (my co-workers at widya wicara) for the very helpful discussion


## 🖤 Acknowledgements
* [DIET-pytorch](https://github.com/cheesama/DIET-pytorch/tree/master/DIET)
* [BERT pretrained](https://github.com/huggingface/transformers)
* [DIET: Lightweight Language Understanding for Dialogue Systems](https://arxiv.org/abs/2004.09936)
