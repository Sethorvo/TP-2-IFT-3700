import numpy as np
import pandas as pd


def read_interval(df: pd.DataFrame):
    pass


def clean_data(df: pd.DataFrame):
    # enlever toutes les pays avec 12 ou plus valeur manquante
    list_of_missing_country = []
    for i in range(len(df.index)):
        if df.iloc[i].isnull().sum() > 11:
            list_of_missing_country.append(df.iloc[i].name)

    return df.drop(list_of_missing_country)


def replace_missing_datas(df: pd.DataFrame):
    dict_median = {}
    for column in df:
        dict_median[column] = df[column].median()

    print(dict_median)


def convert_data_float(df: pd.DataFrame):
    for column in df:

        if df[column].dtype == np.object or df[column].dtype == np.string_:
            df[column] = df[column].str.rstrip('*')
            df[column] = df[column].str.rstrip('[1]')
        # find first not value as null
        is_pourcent = False

        for i in range(len(df.index)):
            # change special character or empty row making cast impossible
            if df[column].iloc[i] == '—' or df[column].iloc[i] == '–' or df[column].iloc[i] == '':
                df[column].iloc[i] = np.nan
            #
            is_pourcent = is_pourcent or (isinstance(df[column].iloc[i], str) and df[column].iloc[i][-1] == "%")

        if is_pourcent:
            df[column] = df[column].str.rstrip('%').astype('float') / 100.0
        else:
            df[column] = df[column].astype('float')
