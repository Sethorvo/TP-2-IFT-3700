from typing import List
import matplotlib.pyplot as plt
import pandas as pd


def find_biggest_correlation(df: pd.DataFrame) -> List:
    df_corr = abs(df.corr(method='spearman'))
    best_correlation = []

    for column in df_corr.columns:
        max_corr = (0, 0, "")
        for i in range(len(df_corr.index)):
            row_name = df_corr.index[i]
            if max_corr[0] < df_corr[column].iloc[i] and row_name != column:
                max_corr = (df_corr[column].iloc[i], i, row_name)

        best_correlation.append(max_corr[1])

    return best_correlation


def order_correlation(df: pd.DataFrame) -> List:
    average_correlation = calculate_average_correlation(df)
    list_of_average_correlation = average_correlation.to_numpy().tolist()
    list_of_average_correlation = [(i, list_of_average_correlation[i]) for i in range(len(list_of_average_correlation))]
    list_of_average_correlation.sort(key=lambda x: x[1], reverse=True)
    return [my_truple[0] for my_truple in list_of_average_correlation]


def calculate_average_correlation(df: pd.DataFrame):
    df_corr = abs(df.corr(method='spearman'))
    return df_corr.mean(axis=0)


def make_histogram(df: pd.DataFrame):
    i = 1
    for colunm in df.columns:
        plt.hist(df[colunm])  # density=False would make counts
        plt.title(colunm)
        plt.savefig(f'../images/corr_{i}.jpg')
        plt.close()
        i += 1
