import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


def find_best_linear_regression(df: pd.DataFrame):
    df_means = df.mean() # might not need it
    df_std =  df.std()
    for column in df.columns:
        y = df[column]
        x = df.loc[:, df.columns != column]
        data_point_x, data_point_x_test, data_point_y, data_point_y_test = train_test_split(x, y, test_size=0.4)
        regression = sm.OLS(data_point_y,data_point_x).fit()
        params_coff = regression.params
        # regression.summary()
        # predictions = regression.predict(data_point_x_test)

        #calculer l'impact, donc normalisé
        impact={}
        for key in params_coff.keys():
            impact[key] = params_coff[key]/df_std[key]

        continue



    return df


