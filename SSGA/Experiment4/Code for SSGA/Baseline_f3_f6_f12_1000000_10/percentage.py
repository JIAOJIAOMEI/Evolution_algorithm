#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
df_com = df_com

opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 10, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
       -10.4028, -10.5363]


def read_file(name):
    df1 = pd.read_csv(name, index_col=[0, 1], header=0)
    return df1


file_name = ["combined_f3612.csv", "combined_f11822.csv"]
df = [read_file(name) for name in file_name]
df = pd.concat(df, axis=0)
df = df.rename_axis(index=["Function", "Times"])
display(df)


def plot_overview(Function, num_com, optimal):
    dataframe = df.loc[(Function, slice(None)), :]
    if Function in ["F2", "F3", "F4", "F5", "F6", "F7", "F9", "F10", "F11", "F12", "F13", "F14"]:
        dataframe = dataframe.round(1)
    elif Function in ["F17"]:
        dataframe = dataframe.round(3)
    elif Function in ["F19", "F20"]:
        dataframe = dataframe.round(2)
    elif Function in ["F8", "F15", "F16", "F21", "F22", "F23"]:
        dataframe = dataframe.round(4)
    elif Function in ["F1", "F18"]:
        dataframe = dataframe.round(5)

    dataframe = pd.DataFrame(data=dataframe.values, columns=dataframe.columns)
    columns = dataframe.columns.tolist()[:num_com]
    percent_dataframe = dataframe.loc[:, dataframe.columns != "Type"].applymap(
        lambda x: True if x == optimal else False)
    percent_dataframe["Type"] = dataframe["Type"]
    percent_df = percent_dataframe.groupby(["Type"]).sum().applymap(lambda x: x * 10)
    percent_df.columns = np.arange(1, 201, 1)
    # percent_df.to_csv("./percent_{0}.csv".format(Function), header=True, index=True)
    # display(percent_df)

    dataframe = percent_df.stack()
    dataframe = dataframe.rename_axis(index=["Type", "Combinations"])
    dataframe = dataframe.reset_index(level=[0, 1], name="Percentage")
    display(dataframe)

    plt.figure(figsize=(20, 5))
    sns.lineplot(data=dataframe, x="Combinations", y="Percentage", hue="Type")
    plt.savefig("./Ex4_{0}1.png".format(Function), dpi=1000)
    plt.show()

    # i = 1
    # max_value = dataframe.max(axis=0)
    # min_value = dataframe.min(axis=0)
    #
    # dist_cols = 4
    # dist_rows = 72
    # plt.figure(figsize=(6 * dist_cols, 6 * dist_rows))
    # for col in columns:
    #     ax = plt.subplot(dist_rows, dist_cols, i)
    #     ax = sns.histplot(data=dataframe, x=col, hue="Type", multiple="dodge", stat="count",
    #                       binrange=(min_value[col], max_value[col]),
    #                       binwidth=(max_value[col] - min_value[col]) / 15 + 0.0001)
    #     ax.set_xlabel("parameter conbination" + str(i))
    #     ax.set_ylabel("Count of optimals")
    #     i = i + 1
    # plt.savefig("./data_analysis_{0}.pdf".format(Function), dpi=1000)
    # plt.show()


flst = ["F1", "F3", "F6", "F12", "F18", "F22"]
optlst = [0, 3, 5, 11, 17, 21]
for i in range(6):
    plot_overview(Function=flst[i], num_com=200, optimal=opt[optlst[i]])
