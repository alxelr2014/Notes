import numpy as np
from LinearClassifier.linear_classifier import score

def eval_classifier(learner, data_train, labels_train, data_test, labels_test):
    th, th_0 = learner(data_train, labels_train)
    n_test = np.shape(data_test)[1]
    score_test = score(data = data_test,labels= labels_test,ths = th, th0s = th_0)
    return score_test / n_test

def eval_learning_alg(learner, data_gen, n_train, n_test, it):
    score_test = 0.0
    for _i in range(it):
        data_train , labels_train = data_gen(n_train)
        data_test , labels_test = data_gen(n_test)
        score_test += eval_classifier(learner,data_train,labels_train, data_test, labels_test)
    return score_test / it

def eval_learning_alg_train(learner, data_gen ,n_train ,it):
    score_test = 0.0
    for _i in range(it):
        data_train, labels_train = data_gen(n_train)
        score_test += eval_classifier(learner,data_train,labels_train, data_train, labels_train)
    return score_test /it


def xval_learning_alg(learner, data, labels, k):
    #cross validation of learning algorithm
    divided_data = np.array_split(data,k,axis = 1)
    divided_label = np.array_split(labels, k , axis = 1)
    score_test = 0.0
    for _i in range(k):
        union_data = np.concatenate([divided_data[_j] for _j in range(k) if _j != _i],axis = 1)
        union_label = np.concatenate([divided_label[_j] for _j in range(k) if _j != _i] , axis = 1)
        score_test += eval_classifier(learner,union_data,union_label, divided_data[_i], divided_label[_i])
    return score_test / k
