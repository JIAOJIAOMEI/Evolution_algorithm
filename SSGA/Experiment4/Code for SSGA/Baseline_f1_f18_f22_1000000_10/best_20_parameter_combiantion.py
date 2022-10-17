# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/16/22 18:22

import numpy as np
from IPython.core.display_functions import display
import pandas as pd

pd.options.display.float_format = '{:.4f}'.format
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

com_file = "./Linear_combination_crossover_normal/combinations_result_baseline.csv"
df_com = pd.read_csv(com_file, header=0)
df_com = df_com[:200]

opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 10, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
       -10.4028, -10.5363]

file_name = ["Linear_combination_crossover_normal",
             "Linear_combination_crossover_uniform",
             "Probabilistic_crossover_normal",
             "Probabilistic_crossover_uniform",
             "singe_point_crossover_normal",
             "singe_point_crossover_uniform"]


def read_file(name):
    path = "./" + name + "/Baseline_table_long_100.csv"
    df1 = pd.read_csv(path, index_col=[0, 1], header=0)
    path2 = "./" + name + "/Baseline_table_long_100_200.csv"
    df2 = pd.read_csv(path2, index_col=[0, 1], header=0)
    # path3 = "./" + name + "/Baseline_table_long_200_end.csv"
    # df3 = pd.read_csv(path3, index_col=[0, 1], header=0)
    # df1 = pd.concat([df1, df2, df3], axis=1)
    df1 = pd.concat([df1, df2], axis=1)
    df1.columns = [i for i in range(0, len(df_com))]
    df1["Type"] = name
    return df1


df = [read_file(name) for name in file_name]
df = pd.concat(df, axis=0)
display(df.shape,df.head(5))
df = df.rename_axis(index=["Function", "Times"])
df = df.sort_index(level="Function")


# display(df)


def best_20(Function):
    dataframe = df.loc[(Function, slice(None)), :]
    if Function in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F10", "F11", "F12", "F13", "F14", "F18"]:
        dataframe = dataframe.round(1)
    elif Function in ["F17"]:
        dataframe = dataframe.round(3)
    elif Function in ["F19", "F20"]:
        dataframe = dataframe.round(2)
    elif Function in ["F8", "F15", "F16", "F21", "F22", "F23"]:
        dataframe = dataframe.round(4)

    dataframe = pd.DataFrame(data=dataframe.values,
                             columns=dataframe.columns)
    dataframe.loc["sum"] = dataframe.loc[:, dataframe.columns != "Type"].sum(axis=0)
    # display(dataframe)
    dataframe = dataframe.sort_values(by="sum", axis=1, ascending=True, na_position="last")
    # display(dataframe)
    k = dataframe.columns.tolist()[:20]
    return k

best_list=[]
for i in [1, 18, 22]:
    best_ = best_20(Function="F" + str(i))
    best_list.append(best_)
display(best_list)
