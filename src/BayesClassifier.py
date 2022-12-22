import os
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


# 3. a)
# return_matrix[i][j] returns the accuracy score if you use naive bayes to
# predict column j with column i of data array (countries)
def get_bayes_prediction_scores(data: np.array, split: float):
    return_matrix = np.copy(data)
    nb_test = int(split * data.shape[0])  # for train / test split
    print(nb_test)
    return_matrix = return_matrix * 0  # set all elements to zero
    bayes_classifier = GaussianNB()  # initiate gaussian bayes classifier
    for i in range(return_matrix.shape[0]):
        for j in range(return_matrix.shape[1]):
            bayes_classifier.fit(data[0:nb_test, i], data[0:nb_test, j])
            prediction = bayes_classifier.predict(data[nb_test:, j])
            return_matrix[i][j] = metrics.accuracy(prediction, data[nb_test:, j])
    return return_matrix


# 3. b)
def get_best_pair_for_each(score_matrix):
    # do this in order to ignore the diagonal of the matrix
    np.fill_diagonal(score_matrix, -1)
    return np.argpartition(score_matrix, axis=0)[0:2, :]


# 3. c)
def get_best_two(score_matrix):
    # do this in order to ignore the diagonal of the matrix
    np.fill_diagonal(score_matrix, 0)
    mean_scores = np.mean(score_matrix, axis=1)

    return np.argpartition(mean_scores, axis=0)[0:2,:]


def test():
    countries = np.random.rand(10,40)
    predictions = get_bayes_prediction_scores(countries, 0.8)
    print( predictions )
    print(get_best_pair_for_each(predictions))
    print(get_best_two(predicitons))

test()

