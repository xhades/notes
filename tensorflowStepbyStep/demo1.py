
"""
@Time: 17-7-13 
@author: xhades
@version: v0.1
@python version : v3.x

使用tf简单训练一个线性函数
"""

import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

biases = tf.Variable(tf.zeros([1]), name='www')
y = Weights*x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)   # 定义优化器 优化算法自选
train = optimizer.minimize(loss)   # 最小化误差

# init = tf.initialize_all_variables()   版本更新后废弃
init = tf.global_variables_initializer()  # 初始化变量
sess = tf.Session()
sess.run(init)  # 初始化  将session的指针放到init上 run


for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

