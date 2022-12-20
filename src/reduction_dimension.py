import numpy as np
import pandas as pd
from sklearn.manifold import Isomap
from matplotlib import pyplot
from sklearn.decomposition import KernelPCA


def execute_question4(df: pd.DataFrame):
    questiona = caculate_pcoa(df)
    plot_result_2d(questiona, "questiona", df.index.tolist())


def calculate_isomap(datas, number_components=2):
    isomap = Isomap(n_components=number_components).fit(datas)
    return isomap.transform(datas)


def caculate_pcoa(datas, number_components=2):
    pcoa = KernelPCA(n_components=number_components).fit(datas)
    return pcoa.transform(datas)


def plot_result_2d(data_set, data_name, column_names):
    # # big  image to be able to read something
    # fig = pyplot.figure(figsize=(384, 216), dpi=100)

    # low quality image to be able to see the bigger picture
    fig = pyplot.figure()
    ax = fig.add_subplot()
    ax.set_title(data_name)
    x = [tuple_[0] for tuple_ in data_set]
    y = [tuple_[1] for tuple_ in data_set]
    ax.scatter(x, y)

    for i, name in enumerate(column_names):
        ax.annotate(name, (x[i], y[i]), fontsize=12)

    pyplot.savefig(f'{data_name}.jpg')
    pyplot.close()
