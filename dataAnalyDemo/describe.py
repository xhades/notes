# !usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np
from scipy.stats import scoreatpercentile


data = np.loadtxt("data.csv", delimiter=',', usecols=(1, ), skiprows=1, unpack=True)

print "MAX method", data.max()