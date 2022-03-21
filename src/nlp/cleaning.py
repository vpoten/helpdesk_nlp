import re

import nltk
from nltk.tokenize import word_tokenize
import gensim


def clean_text(text):
    tokens = word_tokenize(text)
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    return ' '.join(words)


def utils_preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):
    """
    Preprocess a string

    :param text: {string} the text to preprocess
    :param flg_stemm: {bool} whether stemming is to be applied
    :param flg_lemm: {bool} whether lemmitisation is to be applied
    :param lst_stopwords: {list} list of stopwords to remove
    :return: {string} cleaned text
    """
    # clean (convert to lowercase and remove punctuations and characters and then strip)
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())

    # Tokenize (convert from string to list)
    lst_text = text.split()  # remove Stopwords
    if lst_stopwords is not None:
        lst_text = [word for word in lst_text if word not in lst_stopwords]

    # Stemming (remove -ing, -ly, ...)
    if flg_stemm is True:
        ps = nltk.stem.porter.PorterStemmer()
        lst_text = [ps.stem(word) for word in lst_text]

    # Lemmatisation (convert the word into root word)
    if flg_lemm is True:
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        lst_text = [lem.lemmatize(word) for word in lst_text]

    # back to string from list
    text = " ".join(lst_text)
    return text


def list_of_unigrams(text_column):
    """
    Creates a list of list of unigrams

    :param text_column: pd.Series containing preprocessed strings
    :return: list of list
    """
    lst_corpus = []
    for string in text_column:
        lst_words = string.split()
        lst_grams = [" ".join(lst_words[i:i + 1])
                     for i in range(0, len(lst_words), 1)]
        lst_corpus.append(lst_grams)
    return lst_corpus


def build_bigrams_detector(lst_corpus):
    # TODO
    bigrams_detector = gensim.models.phrases.Phrases(lst_corpus, delimiter=" ".encode(), min_count=5, threshold=10)
    return gensim.models.phrases.Phraser(bigrams_detector)


def build_trigrams_detector(lst_corpus, bigrams_detector):
    # TODO
    trigrams_detector = gensim.models.phrases.Phrases(bigrams_detector[lst_corpus], delimiter=" ".encode(), min_count=5,
                                                      threshold=10)
    return gensim.models.phrases.Phraser(trigrams_detector)
