import os

import numpy as np
import pandas as pd  # to work with csv files
from sklearn import feature_extraction, model_selection, naive_bayes, pipeline, manifold, preprocessing
from nltk.corpus import stopwords
import gensim

import src.nlp.cleaning as cleaning

if __name__ == "__main__":
    stop_words = stopwords.words('english')

    our_data = pd.read_csv(os.path.join('/home/victor/DemoProjects/helpdesk_nlp/downloads', 'dataset_clean.csv'))


    def filter_dataset(df):
        df = df[(df['language'] == 'en') & (df['text'] != '') & (df['c3'].notnull()) & (df['c3'] != 'rest')]
        return df


    print(our_data.shape)

    our_data = filter_dataset(our_data)

    print(our_data.shape)

    our_data["text_clean"] = our_data["text"].apply(
        lambda x: cleaning.utils_preprocess_text(x, flg_stemm=False, flg_lemm=True, lst_stopwords=stop_words))

    # convert c3 to a numerical variable
    our_data['label'] = our_data.c3.map(
        {'dev_ateam': 0, 'dev_avengers': 1, 'dev_gondor': 2, 'dev_mordor': 3, 'dev_plugins': 4, 'dev_fe': 5})
    our_data = our_data[["text_clean", "label"]]  # Let us take only the two columns we need.

    # Step 1: train-test split
    X = our_data.text_clean  # the column text contains textual data to extract features from
    y = our_data.label  # this is the column we are learning to predict.
    print(X.shape, y.shape)
    # split X and y into training and testing sets. By default, it splits 75% training and 25% test
    # random_state=1 for reproducibility
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=1)
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    # Train the word2vec model (using only training text)
    lst_X_train = cleaning.list_of_unigrams(X_train)
    w2v_model = gensim.models.Word2Vec(lst_X_train, vector_size=100, window=5, min_count=5)

    # Generate aggregated sentence vectors based on the word vectors for each word in the sentence
    words = set(w2v_model.wv.index_to_key)
    X_train_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words]) for ls in lst_X_train], dtype=object)
    lst_X_test = cleaning.list_of_unigrams(X_test)
    X_test_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words]) for ls in lst_X_test], dtype=object)

    # Why is the length of the sentence different than the length of the sentence vector?
    for i, v in enumerate(X_train_vect):
        print(len(X_train.iloc[i]), len(v))

    # Compute sentence vectors by averaging the word vectors for the words contained in the sentence
    X_train_vect_avg = []
    for v in X_train_vect:
        if v.size:
            X_train_vect_avg.append(v.mean(axis=0))
        else:
            X_train_vect_avg.append(np.zeros(100, dtype=float))

    X_test_vect_avg = []
    for v in X_test_vect:
        if v.size:
            X_test_vect_avg.append(v.mean(axis=0))
        else:
            X_test_vect_avg.append(np.zeros(100, dtype=float))

    # Are our sentence vector lengths consistent?
    for i, v in enumerate(X_train_vect_avg):
        print(len(X_train.iloc[i]), len(v))
