# !/usr/bin/env python
# -*-coding:utf-8-*-

"""
@author: xhades
@Date: 2017/7/23

"""

import nltk
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# 数据清洗 标识化 词干提取

def preprocessing(text):
    text = text.decode("utf-8")
    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]

    preprocessed_text = " ".join(tokens)
    return preprocessed_text




if __name__ == "__main__":
    pass
