import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def read_interval(value_in_string: str):
    # interval entre 0 et la valeur
    if value_in_string[0] == "<":
        return (float(value_in_string[1:])) / 2

    # multiple type of -
    values = value_in_string.split("–")
    if len(values) == 1:
        values = value_in_string.split("-")
    if len(values) == 1:
        values = value_in_string.split("/")
    if len(values) == 1:
        values = value_in_string.split("/")

    if len(values) == 2 and values[0] != "":
        newValues = values[0].split("/")
        values[0] = newValues[0]
        if len(newValues) == 2:
            values[0] = (float(newValues[0]) + float(newValues[1])) / 2

        return (float(values[0]) + float(values[1])) / 2

    return value_in_string


def clean_data(df: pd.DataFrame):
    # enlever toutes les pays avec 12 ou plus valeur manquante
    list_of_missing_country = []
    for i in range(len(df.index)):
        if df.iloc[i].isnull().sum() > 11:
            list_of_missing_country.append(df.iloc[i].name)

    return df.drop(list_of_missing_country)


def replace_missing_datas(df: pd.DataFrame):
    for column in df:
        median = df[column].median()
        df[column] = df[column].fillna(median)


def convert_data_float(df: pd.DataFrame):
    for column in df:
        # delete all character that made cast impossible and are not usefull
        if df[column].dtype == np.object or df[column].dtype == np.string_:
            df[column] = df[column].str.rstrip('*')
            df[column] = df[column].str.rstrip('+')
            df[column] = df[column].str.replace(',000', '000', regex=True)
            df[column] = df[column].str.replace(' \(boys\)', '', regex=True)
            df[column] = df[column].str.replace(' \(girls\), ', '-', regex=True)
            df[column] = df[column].str.replace(r'\[.*\]', '', regex=True)
            df[column] = df[column].str.replace('−', '-', regex=True)
            # age fédéral pour usa
            df[column] = df[column].str.replace('varies by state', '11')

        is_percent = False
        for i in range(len(df.index)):
            if isinstance(df[column].iloc[i], str):
                if df[column].iloc[i] == '—' or df[column].iloc[i] == '–' or df[column].iloc[i] == '' or \
                        df[column].iloc[i] == 'n.a.':
                    # change special character or empty row making cast impossible
                    df[column].iloc[i] = np.nan
                else:
                    # % and interval making cast impossible but some special rule as to be apply
                    is_percent = is_percent or df[column].iloc[i][-1] == "%"
                    df[column].iloc[i] = read_interval(df[column].iloc[i])

        if is_percent:
            df[column] = df[column].str.rstrip('%').astype('float') / 100.0
        else:
            df[column] = df[column].astype('float')


def describe_data(df: pd.DataFrame):
    describe = df.describe(percentiles=[0.5], include='all')
    return describe


def filled_with_regression_multiple_time(df: pd.DataFrame, df_to_filled: pd.DataFrame, number_of_time):
    for i in range(number_of_time):
        df = filled_with_regression(df, df_to_filled)
    return df


def filled_with_regression(df: pd.DataFrame, df_to_filled: pd.DataFrame):
    for column in df.columns:
        y = df[column]
        x = df.loc[:, df.columns != column]
        regression = LinearRegression().fit(x, y)
        for i in range(len(df.index)):
            if df_to_filled[column].iloc[i] == True:
                df[column].iloc[i] = regression.predict([x.iloc[i, :]])[0]

    return df
