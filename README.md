

<br />
<h1>
<p align="center">
  <br>Data Copilot
</h1>
  <p align="center">
    <br />
    </p>
</p>

<p align="center">
<a href="https://www.python.org/"><img alt="Actions Status" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p> -->

## 🎯 What is Data Copilot ?
Data Copilot is AI assistant for data scientist and data analyst for suggest snippets of codes using implementation of Intent and Entity classifier. Data Copilot use DIET for classify user requests (intent and entity) and provide text output in the form of code suggestions. DIET its have means **Dual Intent and Entity Transformer** so the model can predict the intent and entity simultaneously from the input of text. 


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
* [DIET: Lightweight Language Understanding for Dialogue Systems Paper](https://arxiv.org/abs/2004.09936)
