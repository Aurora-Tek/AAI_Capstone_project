
# NIH Chest X-rays Classifier with Deep Learning 

## Dataset 

* Oirignal dataset https://nihcc.app.box.com/v/ChestXray-NIHCC 

## Folder Structure 

```
├── models # Folder with models code 
    └── cnn_tabular_multilabel # Multilable, hybrid CNN model iteration
    └── efficienet # Model with pretrained Efficient model  
    └── iterations # Additional models used for debugging and hypothesis testing 
├── DataPreprocessing-EDA.ipynb - EDA and Data-preprocessing notebook
├── Preprocesing_Pipeline.ipynb - Shared preprocessing steps for Hybrid and EfficientNet training 
└── image_scale.py # Script for scaling images using multithreading

```

