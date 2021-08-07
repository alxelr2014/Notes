import code_and_data_for_hw3.code_for_hw3_part2 as supplement
import time


def auto_test():
    possible_T = [1, 10, 50]
    feature1 = [('cylinders', supplement.raw),
                ('displacement', supplement.raw),
                ('horsepower', supplement.raw),
                ('weight', supplement.raw),
                ('acceleration', supplement.raw),
                ('origin', supplement.raw)]

    feature2 = [('cylinders', supplement.one_hot),
                ('displacement', supplement.standard),
                ('horsepower', supplement.standard),
                ('weight', supplement.standard),
                ('acceleration', supplement.standard),
                ('origin', supplement.one_hot)]
    possible_features = [feature1, feature2]

    _i = 0
    __i = 1

    auto_data = supplement.load_auto_data("C:/Users/emadz/Desktop/School/Books/Summer II/Machine "
                                          "Learning/Workspace/Codes/Features/code_and_data_for_hw3/auto-mpg.tsv")
    in_data, in_labels = supplement.auto_data_and_labels(auto_data, possible_features[__i])
    # print(supplement.xval_learning_alg(supplement.perceptron, in_data, in_labels, 10, params={'T': possible_T[
    # _i]})) print(supplement.xval_learning_alg(supplement.averaged_perceptron, in_data, in_labels, 10, params={'T':
    # possible_T[ _i]}))

    print(supplement.averaged_perceptron(in_data, in_labels, params={'T': possible_T[_i]}))


def review_test():
    review_data = supplement.load_review_data("C:/Users/emadz/Desktop/School/Books/Summer II/Machine "
                                              "Learning/Workspace/Codes/Features/code_and_data_for_hw3/reviews.tsv")
    # seperates the data
    review_texts, review_label_list = zip(*((sample['text'], sample['sentiment']) for sample in review_data))

    # The dictionary of all the words for "bag of words"
    dictionary = supplement.bag_of_words(review_texts)

    # The standard data arrays for the bag of words
    review_bow_data = supplement.extract_bow_feature_vectors(review_texts, dictionary)
    review_labels = supplement.rv(review_label_list)

    possible_T = [1, 10, 50]

    # for t in possible_T:
    #     start = time.time()
    #     print(supplement.xval_learning_alg(supplement.perceptron,
    #     review_bow_data, review_labels, 10, params={'T': t}))
    #     end = time.time()
    #     print(end - start)
    #     start = time.time()
    #     print(supplement.xval_learning_alg(supplement.averaged_perceptron, review_bow_data, review_labels, 10,
    #                                        params={'T': t}))
    #     end = time.time()
    #     print(end - start)
    #     print()

    bestTh, bestTh0 = supplement.averaged_perceptron(review_bow_data, review_labels, params={'T': 10})
    sorted_th = sorted([(x, i) for (i, x) in enumerate(bestTh)], reverse=True)
    # print(sorted_th)
    positive_words = [list(dictionary.keys())[list(dictionary.values()).index(i)] for (x, i) in sorted_th[:10]]
    print(positive_words)
    negative_words = [list(dictionary.keys())[list(dictionary.values()).index(i)] for (x, i) in sorted_th[-10:]]
    print(negative_words)


review_test()
