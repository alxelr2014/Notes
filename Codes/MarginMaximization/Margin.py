import numpy as np


def margin(x, y, th, th0):
    return y * (np.dot(th.T, x) + th0)


def sum_objective(data, label, th, th0):
    answer = [0]
    n = data.shape[1]
    for _i in range(n):
        x = np.array(data[:, _i])
        y = np.array(label[:, _i])
        answer += margin(x, y, th, th0)
    return answer


def min_objective(data, label, th, th0):
    n = data.shape[1]
    answer = [margin(np.array(data[:, _i]), np.array(label[:, _i]), th, th0) for _i in range(n)]
    return min(answer)


def max_objective(data, label, th, th0):
    n = data.shape[1]
    answer = [margin(np.array(data[:, _i]), np.array(label[:, _i]), th, th0) for _i in range(n)]
    return max(answer)


def comparison():
    data = np.array([[1, 2, 1, 2, 10, 10.3, 10.5, 10.7],
                     [1, 1, 2, 2, 2, 2, 2, 2]])
    labels = np.array([[-1, -1, 1, 1, 1, 1, 1, 1]])
    blue_th = np.array([[0, 1]]).T
    blue_th0 = -1.5
    red_th = np.array([[1, 0]]).T
    red_th0 = -2.5
    answer1 = [sum_objective(data, labels, red_th, red_th0)[0], min_objective(data, labels, red_th, red_th0)[0],
               max_objective(data, labels, red_th, red_th0)[0]]
    print(answer1)
    answer2 = [sum_objective(data, labels, blue_th, blue_th0)[0], min_objective(data, labels, blue_th, blue_th0)[0],
               max_objective(data, labels, blue_th, blue_th0)[0]]
    print(answer2)


comparison()
