# Chatbot-gemma

## How to install
- Go to https://www.kaggle.com/models/google/gemma and download the keras version of the model
- Extract the tar.gz file in the model directory: ```tar -xzf gemma-keras-gemma_1.1_instruct_2b_en-v3.tar.gz ./model```
- Run the web app using flask: ```flask --app api run```


Instead you can use this python script to download Gemma 1 from kagglehub
```python
import kagglehub

# Download latest version
path = kagglehub.model_download("keras/gemma/keras/gemma_1.1_instruct_2b_en")

print("Path to model files:", path)
```
