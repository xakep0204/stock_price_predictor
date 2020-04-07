import tensorflow as tf
import numpy as np
import pandas
import matplotlib.pyplot as plt
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
