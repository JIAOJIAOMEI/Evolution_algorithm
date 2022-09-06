# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/18/22 01:03
import numpy as np
import pandas as pd
from IPython.core.display_functions import display
import seaborn as sns
from matplotlib import pyplot as plt

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# opt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -418.98 * 50, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.00030, -1.0316, 0.398, 3.0,
#        -3.86, -3.32, -10.1532,
#        -10.4028, -10.5363]
#
# path = "Lamarck_table_long_1_3072.csv"
# df = pd.read_csv(path, index_col=[0, 1], header=0)
#
#
# def percent(Function, optimal):
#     dataframe = df.loc[(Function, slice(None)), :]
#     if Function in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F10", "F11", "F12", "F13", "F14", "F18"]:
#         dataframe = dataframe.round(1)
#     elif Function in ["F17"]:
#         dataframe = dataframe.round(3)
#     elif Function in ["F19", "F20"]:
#         dataframe = dataframe.round(2)
#     elif Function in ["F8", "F15", "F16", "F21", "F22", "F23"]:
#         dataframe = dataframe.round(4)
#
#     dataframe = pd.DataFrame(data=dataframe.values,
#                              columns=dataframe.columns)
#     percent_dataframe = dataframe.applymap(lambda x: True if x <= optimal else False)
#     # !!!!!!!!<=
#     percent_dataframe["Function"] = Function
#     return percent_dataframe
#
#
# function_list = np.arange(1, 24, 1)
# percent_df = [percent(Function="F" + str(i), optimal=opt[i - 1]) for i in function_list]
# percent_df = pd.concat(percent_df, axis=0)
# percent_df = percent_df.groupby(["Function"]).sum().applymap(lambda x: str(x*10)+"%" )
# index = ["F" + str(i) for i in range(1, 24, 1)]
# percent_df = percent_df.loc[index]
# display(percent_df)
#
#
# percent_df.to_csv("./Experiment1_Lamarck.csv")

dataframe1 = pd.read_csv("./Experiment1_Baldwin1.csv", index_col=[0], header=0)
dataframe1.columns = [i for i in range(1, 3073, 1)]
dataframe2 = pd.read_csv("./Experiment1_Lamarck1.csv", index_col=[0], header=0)
dataframe2.columns = [i for i in range(1, 3073, 1)]
dataframe = pd.concat([dataframe1, dataframe2], axis=0, keys=["Baldwin", "Lamarck"])

dataframe = dataframe.stack()

dataframe = dataframe.rename_axis(index=["Mode", "Function", "Combinations"])
dataframe = dataframe.reset_index(level=[0, 2], name="Percentage")
dataframe = dataframe.reset_index(drop=False)
display(dataframe)

function_list = ["F" + str(i) for i in range(1, 24, 1)]


def show_graph(dataframe):
    sns.set()
    dist_cols = 1
    dist_rows = 23
    plt.figure(figsize=(12 * dist_cols, 6 * dist_rows))
    i = 1
    for function in function_list:
        dataf = dataframe[dataframe["Function"] == function]
        display(dataf)
        ax = plt.subplot(dist_rows, dist_cols, i)
        sns.relplot(data=dataf, x="Combinations", y="Percentage", hue="Mode")
        i = i + 1
        plt.savefig("./Ex1_1{0}.png".format(function), dpi=1000)
        plt.show()


show_graph(dataframe=dataframe)
