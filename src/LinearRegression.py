import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression


def find_best_linear_regression(df: pd.DataFrame):
    for column in df.columns:
        y = df[column]
        x = df.loc[:, df.columns != column]
        data_point_x, data_point_x_test, data_point_y, data_point_y_test = train_test_split(x, y, test_size=0.4)
        regression = LinearRegression().fit(data_point_x, data_point_y)
        predictions = regression.predict(data_point_x_test)

        fs = SelectKBest(score_func=f_regression, k=2)
        # learn relationship from training data
        fs.fit(data_point_x, data_point_y)
        # transform train input data
        X_train_fs = fs.transform(data_point_x)
        # transform test input data
        X_test_fs = fs.transform(data_point_x_test)

        continue

    return df
