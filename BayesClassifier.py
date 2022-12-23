import os
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


# 3. a)
# return_matrix[i][j] returns the accuracy score if you use naive bayes to
# predict column j with column i of data array (countries)
def get_bayes_prediction_scores(data, split):
    return_matrix = np.zeros(shape=(data.shape[1], data.shape[1]))
    nb_test = int(data.shape[0] * split)  # for train / test split
    return_matrix = return_matrix * 0  # set all elements to zero
    bayes_classifier = MultinomialNB()  # initiate multinomial bayes classifier
    for i in range(return_matrix.shape[1]):
        for j in range(return_matrix.shape[1]):
            bayes_classifier.fit(data[0:nb_test, i].reshape(-1, 1), data[0:nb_test, j].reshape(-1, 1))
            prediction = bayes_classifier.predict(data[nb_test:, i].reshape(-1, 1))
            return_matrix[i][j] = metrics.accuracy_score(prediction, data[nb_test:, j])
    return return_matrix


# 3. b)
def get_best_pair_for_each(score_matrix):
    # do this in order to ignore the diagonal of the matrix
    np.fill_diagonal(score_matrix, -1)
    return np.argsort(score_matrix, axis=0)[0:2, :].T


# 3. c)
def get_best_two(score_matrix):
    # do this in order to ignore the diagonal of the matrix
    np.fill_diagonal(score_matrix, 0)
    mean_scores = np.mean(score_matrix, axis=1)
    return np.argsort(mean_scores, axis=0)[0:2]
