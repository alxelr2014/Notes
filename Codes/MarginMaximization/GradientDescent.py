import numpy as np


def gd(f, df, x0, step_size_fn, max_iter):
    """f: a function whose input is an x, a column vector, and returns a scalar.
    df: a function whose input is an x,
    a column vector, and returns a column vector representing the gradient of f at x.
    x0: an initial value of x, which is a column vector.
    step_size_fn: a function that is given the iteration index (an integer) and returns a step size.
    max_iter: the number of iterations to perform """
    x = x0.copy()
    fx = f(x)
    xs = [x]
    fs = [fx]
    for _i in range(max_iter):
        x = x - step_size_fn(_i + 1) * df(x)
        fx = f(x)
        xs.append(x)
        fs.append(fx)
    return x, fs, xs


def num_grad(f, delta=0.001):
    def df(x):
        n = x.shape[0]
        delta_vector = np.zeros((n, 1))
        res = np.zeros((n, 1))
        for _i in range(n):
            delta_vector[_i][0] = delta
            res[_i][0] = (f(x + delta_vector) - f(x - delta_vector)) / (2 * delta)
            delta_vector[_i][0] = 0
        return res

    return df


def f1(x):
    return float((2 * x + 3) ** 2)


def f2(v):
    x = float(v[0])
    y = float(v[1])
    return (x - 2.) * (x - 3.) * (x + 3.) * (x + 1.) + (x + y - 1) ** 2


x = np.array([[0], [0]])
print(num_grad(f2)(x))
