import numpy as np
from GradientDescent import gd as gd


def hinge(v):
    return np.where(v < 1, 1 - v, 0)


# x is dxn, y is 1xn, th is dx1, th0 is 1x1
def hinge_loss(x, y, th, th0):
    return np.average(hinge(y * (np.dot(th.T, x) + th0)))


# x is dxn, y is 1xn, th is dx1, th0 is 1x1, lam is a scalar
def svm_obj(x, y, th, th0, lam):
    return hinge_loss(x, y, th, th0) + lam * (np.linalg.norm(th)) ** 2


# Returns the gradient of hinge(v) with respect to v.
def d_hinge(v):
    return np.where(v < 1, - 1, 0)


# Returns the gradient of hinge_loss(x, y, th, th0) with respect to th
def d_hinge_loss_th(x, y, th, th0):
    ydh = y * d_hinge(y * (np.dot(th.T, x) + th0))
    return x * ydh


# Returns the gradient of hinge_loss(x, y, th, th0) with respect to th0
def d_hinge_loss_th0(x, y, th, th0):
    return y * d_hinge(y * (np.dot(th.T, x) + th0))


# Returns the gradient of svm_obj(x, y, th, th0) with respect to th
def d_svm_obj_th(x, y, th, th0, lam):
    return np.array([np.average(d_hinge_loss_th(x, y, th, th0), axis=1)]).T + 2 * lam * th


# Returns the gradient of svm_obj(x, y, th, th0) with respect to th0
def d_svm_obj_th0(x, y, th, th0, lam):
    return np.array([[np.average(d_hinge_loss_th0(x, y, th, th0))]]) + lam * 0


# Returns the full gradient as a single vector (which includes both th, th0)
def svm_obj_grad(x, y, th, th0, lam):
    return np.vstack((d_svm_obj_th(x, y, th, th0, lam), d_svm_obj_th0(x, y, th, th0, lam)))


def batch_svm_min(data, labels, lam):
    def svm_min_step_size_fn(i):
        return 2 / (i + 1) ** 0.5

    d = data.shape[0]
    init_val = np.zeros((d + 1, 1))

    def svm_func_obj(x):
        th = np.array(x[:d, :])
        th0 = np.array([x[d, :]])
        return svm_obj(data, labels, th, th0, lam)

    def svm_grad_obj(x):
        th = np.array(x[:d, :])
        th0 = np.array([x[d, :]])
        return svm_obj_grad(data, labels, th, th0, lam)

    return gd(svm_func_obj, svm_grad_obj, init_val, svm_min_step_size_fn, 10)


def super_simple_separable():
    X = np.array([[2, 3, 9, 12],
                  [5, 2, 6, 5]])
    y = np.array([[1, -1, 1, -1]])
    return X, y


def separable_medium():
    X = np.array([[2, -1, 1, 1],
                  [-2, 2, 2, -1]])
    y = np.array([[1, -1, 1, -1]])
    return X, y


sep_m_separator = np.array([[2.69231855], [0.67624906]]), np.array([[-3.02402521]])

x_1, y_1 = super_simple_separable()
ans = batch_svm_min(x_1, y_1, 0.0001)
print(ans)

x_1, y_1 = separable_medium()
ans = batch_svm_min(x_1, y_1, 0.0001)
print(ans)
