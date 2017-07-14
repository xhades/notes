
"""
@Time: 17-7-13 
@author: xhades
@version: v0.1
@python version : v3.x

自定义一个神经层
"""

import tensorflow as tf


def addlayer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_uniform([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if not activation_function:
        outputs = Wx_plus_b

    else:
        outputs = activation_function(Wx_plus_b)

    return outputs




