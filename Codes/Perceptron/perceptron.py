import numpy as np


def perceptron(data, labels, params=None, hook=None):
    # if T not in params, default to 100
    if params is None:
        params = {}
    t = params.get('T', 100)
    d = np.shape(data)[0]
    n = np.shape(data)[1]
    th = np.zeros((d, 1))
    th_0 = np.zeros((1, 1))
    for _i in range(t):
        flag = True
        for __i in range(n):
            if labels[0][__i] * (np.dot(th.T, np.array([data[:, __i]]).T) + th_0)[0][0] <= 0:
                th += labels[0][__i] * np.array([data[:, __i]]).T
                th_0 += np.array([labels[0][__i]])
                flag = False
        if flag:
            break
    return th, th_0


def perceptron_through_origin(data, labels, params):  # modified
    if params is None:
        params = {}
    t = params.get('T', 100)
    d = np.shape(data)[0]
    n = np.shape(data)[1]
    extended_data = np.concatenate((data, np.ones((1, n))), axis=0)
    th = np.zeros((d + 1, 1))
    num_mistakes = 0
    flag = False
    while not flag:
        flag = True
        for __i in range(n):
            if labels[0][__i] * (np.dot(th.T, np.array([extended_data[:, __i]]).T))[0][0] <= 0:
                th += labels[0][__i] * np.array([extended_data[:, __i]]).T
                num_mistakes += 1
                flag = False
    return th, num_mistakes


def averaged_perceptron(data, labels, params=None, hook=None):
    if params is None:
        params = {}
    t = params.get('T', 100)
    d = np.shape(data)[0]
    n = np.shape(data)[1]
    th = np.zeros((d, 1))
    th_0 = np.zeros((1, 1))
    ths = np.zeros((d, 1))
    th_0s = np.zeros((1, 1))
    for _i in range(t):
        for __i in range(n):
            if labels[0][__i] * (np.dot(th.T, np.array([data[:, __i]]).T) + th_0)[0][0] <= 0:
                th += labels[0][__i] * np.array([data[:, __i]]).T
                th_0 += np.array([labels[0][__i]])
            ths += th
            th_0s += th_0
    return ths / (n * t), th_0s / (n * t)


# in_data = np.array([[2, 3, 4, 5]])
# in_label = np.array([[1, 1, -1, -1]])
# print(perceptron(in_data, in_label, params=None))

# in_data = np.array([[0.2, 0.8, 0.2, 0.8], [0.2, 0.2, 0.8, 0.8]])
# in_label = np.array([[-1, -1, 1, 1]])
# print(perceptron_through_origin(in_data, in_label, params=None))
