import pandas as pd


def find_biggest_correlation(df: pd.DataFrame):
    df_corr = abs(df.corr())
    best_correlation = {}

    for column in df_corr.columns:
        max_corr = (0, 0, "")
        for i in range(len(df_corr.index)):
            row_name = df_corr.index[i]
            if max_corr[0] < df_corr[column].iloc[i] and row_name != column:
                max_corr = (df_corr[column].iloc[i], i, row_name)

        best_correlation[column] = max_corr

    return best_correlation


def order_correlation(df: pd.DataFrame):
    average_correlation = calculate_average_correlation(df)
    return average_correlation.sort_values(axis=0, ascending=False)


def calculate_average_correlation(df: pd.DataFrame):
    df_corr = abs(df.corr())
    return df_corr.mean(axis=1)
