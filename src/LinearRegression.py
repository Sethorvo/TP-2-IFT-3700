import os
from pathlib import Path

import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


def find_best_linear_regression(df: pd.DataFrame):
    cwd = Path(os.getcwd())
    file_to_save = cwd.joinpath("summaries.txt")
    with open(file_to_save, 'w') as open_file:
        for column in df.columns:
            y = df[column]
            x = df.loc[:, df.columns != column]
            data_point_x, data_point_x_test, data_point_y, data_point_y_test = train_test_split(x, y, test_size=0.4)
            regression = sm.OLS(data_point_y, data_point_x).fit()
            summary = regression.summary()
            open_file.write(summary)

    return


def normalize_regression(df: pd.DataFrame):
    df_normalized = df.copy()
    for column in df_normalized.columns:
        df_normalized[column] = (df_normalized[column] - df_normalized[column].mean()) / df_normalized[column].std()
    params = {}
    for column in df_normalized.columns:
        y = df_normalized[column]
        x = df_normalized.loc[:, df.columns != column]
        regression = sm.OLS(y, x).fit()
        params[column] = regression.params

    df_temp = pd.DataFrame(params)
    df_temp.to_csv('../params.csv')
