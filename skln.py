#!/usr/bin/env python
#-*-coding:utf-8-*-

import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder

# Breast Cancer Wisconsin dataset

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/'
                 'breast-cancer-wisconsin/wdbc.data', header=None)

print df.head(2)

