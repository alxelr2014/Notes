from  Perceptron.perceptron import  perceptron,averaged_perceptron
from Perceptron.code_for_hw02_downloadable import gen_flipped_lin_separable
from Perceptron.evaluation import  eval_learning_alg,eval_learning_alg_train

n_train = 20
n_test = 20
it = 100
for p in [0.1,0.25]:
	print(eval_learning_alg(perceptron, gen_flipped_lin_separable(pflip=p),n_train,n_test,it))
	print(eval_learning_alg(averaged_perceptron,gen_flipped_lin_separable(pflip=p),n_train,n_test,it))

for p in [0.1,0.25]:
	print(eval_learning_alg_train(perceptron, gen_flipped_lin_separable(pflip=p),n_train,it))
	print(eval_learning_alg_train(averaged_perceptron,gen_flipped_lin_separable(pflip=p),n_train,it))