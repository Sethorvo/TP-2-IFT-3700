import os
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


def linear_regression(df: pd.DataFrame):
    cwd = Path(os.getcwd())
    file_to_save = cwd.joinpath("summaries.txt")
    r_out = {}
    with open(file_to_save, 'w') as open_file:
        for column in df.columns:
            y = df[column]
            x = df.loc[:, df.columns != column]
            data_point_x, data_point_x_test, data_point_y, data_point_y_test = train_test_split(x, y, test_size=0.4)
            # regression = sm.OLS(y, x).fit()
            regression = sm.OLS(data_point_y, data_point_x).fit()
            summary = regression.summary()
            open_file.write(str(summary))
            predictions = regression.predict(data_point_x_test)
            error = sum([pow((predictions[i] - data_point_y_test[i]), 2) for i in range(len(predictions))])
            mean_of_test = data_point_y_test.mean()
            diff_to_mean = sum([pow((data_point_y_test[i] - mean_of_test), 2) for i in range(len(data_point_y_test))])
            r_out[column] = 1 - (error / diff_to_mean)

    print(r_out)
    return


def find_best_linear_regression(df: pd.DataFrame):
    list_of_best_column = []
    for column in df.columns:
        y = df[column]
        columns_to_evaluate = df.columns.tolist().copy()
        columns_to_evaluate.remove(column)
        column_bloc_2 = columns_to_evaluate.copy()
        best_colunm = (0, "", "")

        for column1 in columns_to_evaluate:
            column_bloc_2.remove(column1)
            for column2 in column_bloc_2:
                x = df.loc[:, [column1, column2]]
                data_point_x, data_point_x_test, data_point_y, data_point_y_test = train_test_split(x, y, test_size=0.4)
                regression = sm.OLS(data_point_y, data_point_x).fit()
                predictions = regression.predict(data_point_x_test)
                error = sum([pow((predictions[i] - data_point_y_test[i]), 2) for i in range(len(predictions))])
                mean_of_test = data_point_y_test.mean()
                diff_to_mean = sum(
                    [pow((data_point_y_test[i] - mean_of_test), 2) for i in range(len(data_point_y_test))])
                r_out = 1 - (error / diff_to_mean)
                if best_colunm[0] < r_out:
                    best_colunm = (r_out, column1, column2)

        list_of_best_column.append(best_colunm)

    columns_to_evaluate = df.columns.tolist().copy()
    list_of_int = []
    for item in list_of_best_column:
        new_int = [columns_to_evaluate.index(item[1]), columns_to_evaluate.index(item[2])]
        list_of_int.append(new_int)

    return list_of_int


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
    df_temp.to_csv('params.csv')
