import numpy as np


def getCor(data):
    return np.corrcoef(data)

def getStrongestCorr(corr_matrix):
    return corr_matrix.max(axis=0)

def getOrderCorr(corr_matrix):
    corr_matrix = np.abs(corr_matrix) # get absolute values
    corr_mean_vect = corr_matrix.mean(axis=1) # get the mean of the absolute correlations
    return np.argsort(corr_mean_vect) # get the ordered indices
    