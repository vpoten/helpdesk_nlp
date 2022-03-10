from nltk.tokenize import word_tokenize


def clean_text(text):
    tokens = word_tokenize(text)
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    return ' '.join(words)
