import numpy as np

def length(col_v):
    return np.dot(col_v.T,col_v)[0][0] ** 0.5

def signed_dist(x, th, th0):
    return (np.array(th0) + np.dot(th.T, x))/length(th)

def positive(x, th, th0):
    return np.sign(signed_dist(x,th,th0))

def score(data, labels, ths, th0s):
   pos = np.sign(np.dot(np.transpose(ths), data) + np.transpose(th0s))
   return np.sum(pos == labels, axis = 1, keepdims = True)


def best_separator(data, labels, ths, th0s):
    j = np.argmax( score(data,labels,ths,th0s))
    A = np.array([ths[:,j]]).T , np.array([[th0s[0][j]]])
    return A