import numpy as np
def perceptron(data, labels, params=None, hook=None):
	# if T not in params, default to 100
	if params is None:
		params = {}
	T = params.get('T', 100)
	d = np.shape(data)[0]
	n = np.shape(data)[1]
	th = np.zeros((d, 1))
	th_0 = np.zeros((1, 1))
	for _i in range(T):
		flag = True
		for __i in range(n):
			if labels[0][__i] * (np.dot(th.T, np.array([data[:, __i]]).T) + th_0)[0][0] <= 0:
				th += labels[0][__i] * np.array([data[:, __i]]).T
				th_0 += np.array([labels[0][__i]])
				flag = False
		if flag:
			break
	return th, th_0


def averaged_perceptron(data, labels, params=None, hook=None):
	if params is None:
		params = {}
	T = params.get('T', 100)
	d = np.shape(data)[0]
	n = np.shape(data)[1]
	th = np.zeros((d, 1))
	th_0 = np.zeros((1, 1))
	ths = np.zeros((d, 1))
	th_0s = np.zeros((1, 1))
	for _i in range(T):
		for __i in range(n):
			if labels[0][__i] * (np.dot(th.T, np.array([data[:, __i]]).T) + th_0)[0][0] <= 0:
				th += labels[0][__i] * np.array([data[:, __i]]).T
				th_0 += np.array([labels[0][__i]])
			ths += th
			th_0s += th_0
	return ths / (n * T), th_0s / (n * T)
