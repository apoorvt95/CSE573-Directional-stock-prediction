# Directional Stock Prediction using online news
This is project built as a requirement for course CSE 573 Semantic Web Mining at Arizona State University. The aim is to build directional stock prediction system which predict stock market price movement using online news. It is built using BERT and Bidirectional LSTM. 

## Dataset
The model is trained on a news corpus consisting over 80000 articles related to Amazon and Apple news. The dataset was collected between January 2018 to February 2019. The dataset also contains stock chart price of AMZN and AAPL stocks. We build a labelled dataset utilizing change in stock price at different intervals of time.

## How to setup the project
1. Clone the project. Make sure you have python 3.7 installed in your system.
2. Open a terminal, and change directory to CODE folder. 
3. Run "pip install -r requirements.txt" command. This command should install all the python dependencies required to run the project. After installing dependencies. Open Python terminal, import nltk and run nltk.download('punkt')
4. Download the dataset from [here](https://drive.google.com/drive/folders/1L4onfGFqo4UdeMD2toyqDBxQ_xJkgudg?usp=sharing "Dataset") .You need to request access from us.
5. ExtractedNewsSentenceWise.csv contains sentences wise news for Amazon and Apple stock. The charts folder contains the stock price chart. Download the CHARTS Folder and all the CSVs.  
6. Install Jupyter by running command "pip install jupyter". 
7. For training BERT, run BertTrain.
8. Now you can train either simple models (RandomForest, Decision Trees, Logistic Regression) or Deep Learning Models (B-LSTM). 
9. For training simple models, run ArticleExtraction.
10. For training deep learning models, run DeepLearningModel.

## Evaluations
* We have used accuracy metric, F-Score and ROC to evaluate our model. We attained accuracy of 76% using BERT and B-LSTM. The graph plots are included under EVALUATIONS folder. 
* TODO: We want to evaluate BERT and LSTM with sentence wise dataset. We also want to curate dataset using co-reference resolution.