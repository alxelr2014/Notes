import numpy as np
from Perceptron.perceptron import perceptron


def one_hot(x, k):
    res = np.zeros((k, 1))
    res[x - 1] = 1
    return res


original_data = np.array([[1, 2, 3, 4, 5, 6]])
in_data = np.empty((6, 0))
for _l in original_data[0]:
    in_data = np.append(in_data, one_hot(_l, 6), axis=1)
in_labels = np.array([[1, 1, -1, -1, 1, 1]])
th, th0 = perceptron(in_data, in_labels, params=None)
print(th)
print(th0)
print(np.dot(th.T, one_hot(1, 6)) + th0)
print(np.dot(th.T, one_hot(6, 6)) + th0)
