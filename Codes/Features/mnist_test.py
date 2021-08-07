import code_and_data_for_hw3.code_for_hw3_part2 as supplement
import numpy as np


def row_average_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (m,1) array where each entry is the average of a row
    """
    return np.array([np.average(x, axis=1)]).T


def col_average_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (n,1) array where each entry is the average of a column
    """
    return np.array([np.average(x, axis=0)]).T


def top_bottom_features(x):
    """
    @param x (m,n) array with values in (0,1)
    @return (2,1) array where the first entry is the average of the
    top half of the image = rows 0 to floor(m/2) [exclusive]
    and the second entry is the average of the bottom half of the image
    = rows floor(m/2) [inclusive] to m
    """
    temp = row_average_features(x)
    m = temp.shape[0]
    halved = np.split(temp, [m // 2])
    print(halved)
    return np.array([[col_average_features(halved[0])[0][0]], [col_average_features(halved[1])[0][0]]])


def test_accuracy():
    mnist_data_dict = supplement.load_mnist_data(range(0, 10))
    mnist_data = []
    mnist_labels = []

    for _i in range(0, 10):
        mnist_data += mnist_data_dict[_i]['images']
        mnist_labels += list(mnist_data_dict[_i]['labels'][0])

    for i in range(len(mnist_data)):
        mnist_data[i] = np.reshape(mnist_data[i], (28 * 28, 1))

    # for images in mnist_data:
    #     print(images.shape)
    # supplement.get_classification_accuracy()

    dataset = [(0, 1), (2, 4), (6, 8), (9, 0)]
    answer = []
    for task in dataset:
        data_task = mnist_data_dict[task[0]]['images'] + mnist_data_dict[task[1]]['images']
        print(task)
        for i in range(len(data_task)):
            data_task[i] = np.reshape(data_task[i], (28 * 28, 1))
        data_task_array = np.concatenate(tuple(data_task), axis=1)

        task_labels = list(mnist_data_dict[task[0]]['labels'][0]) + list(mnist_data_dict[task[1]]['labels'][0])
        task_labels = np.array([task_labels])

        print(task_labels.shape)

        answer += [supplement.get_classification_accuracy(data_task_array, task_labels)]
    print(answer)


test_accuracy()
