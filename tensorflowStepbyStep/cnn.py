# -*-coding:utf-8-*-
"""
@Time: 17-7-14 
@author: xhades
@version: v0.1

tensorflow 实现卷积神经网络
"""
import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)