import os
import warnings

warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd  # to work with csv files

# matplotlib imports are used to plot confusion matrices for the classifiers
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# import feature extraction methods from sklearn
from sklearn.feature_extraction.text import CountVectorizer

# pre-processing of text
import string
import re

# import classifiers from sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# import different metrics to evaluate the classifiers
from sklearn.metrics import accuracy_score

# from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics

import sklearn
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

# import time function from time module to track the training duration
from time import time

# import nltk
from nltk.corpus import stopwords

if __name__ == "__main__":
    stop_words = stopwords.words('english')

    our_data = pd.read_csv(os.path.join('/home/victor/DemoProjects/helpdesk_nlp/downloads', 'dataset_clean.csv'))

    def filter_dataset(df):
        df = df[(df['language'] == 'en') & (df['text'] != '') & (df['c1'].notnull())]
        return df

    print(our_data.shape)

    our_data = filter_dataset(our_data)

    print(our_data.shape)

    our_data["c1"].value_counts() / our_data.shape[0]  # Class distribution in the dataset

    # convert c1 to a numerical variable
    our_data['label'] = our_data.c1.map({'development': 1, 'rest': 0})  # development is 1, rest is 0.
    our_data = our_data[["text", "label"]]  # Let us take only the two columns we need.
    print(our_data.shape)


    def clean(doc):  # doc is a string of text
        doc = doc.replace("</br>", " ")  # This text contains a lot of <br/> tags.
        doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])
        doc = " ".join([token for token in doc.split() if token not in stop_words])
        # remove punctuation and numbers
        return doc


    # Step 1: train-test split
    X = our_data.text  # the column text contains textual data to extract features from
    y = our_data.label  # this is the column we are learning to predict.
    print(X.shape, y.shape)
    # split X and y into training and testing sets. By default, it splits 75% training and 25% test
    # random_state=1 for reproducibility
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    # Step 2-3: Preprocess and Vectorize train and test data
    vect = CountVectorizer(preprocessor=clean)  # instantiate a vectoriezer
    X_train_dtm = vect.fit_transform(X_train)  # use it to extract features from training data
    # transform testing data (using training data's features)
    X_test_dtm = vect.transform(X_test)
    print(X_train_dtm.shape, X_test_dtm.shape)
    # i.e., the dimension of our feature vector is 19089!

    # Step 3: Train the classifier and predict for test data
    nb = MultinomialNB()  # instantiate a Multinomial Naive Bayes model
    nb.fit(X_train_dtm, y_train)  # train the model(timing it with an IPython "magic command")
    y_pred_class = nb.predict(X_test_dtm)  # make class predictions for X_test_dtm
