# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/18/22 01:03
import numpy as np
import pandas as pd
from IPython.core.display_functions import display

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
com_df = pd.read_csv("./best_combination_20.csv",
                     header=0,
                     index_col=[0])
# com = com_df.values.tolist()
index = com_df.index.tolist()

# display(com_df.nunique(axis=0))
sheet_name = ["combination" + str(i) for i in index]
opt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -418.98 * 50, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.00030, -1.0316, 0.398, 3.0, -3.86, -3.32, -10.1532,
       -10.4028, -10.5363]


def read_file(sheetname, path):
    df = pd.read_excel(path, sheet_name=sheetname,
                       header=0,
                       index_col=[0, 1])
    df = df.rename_axis(["Function", "Times"])
    return df


path = "Larmack.xlsx"
df = [read_file(name, path) for name in sheet_name]
df = pd.concat(df, axis=1)
df.columns = sheet_name

df.to_csv("./Larmack121_f2_4_5_7_1000000_50d_rawdata.csv")


def percent(Function, optimal):
    dataframe = df.loc[(Function, slice(None)), :]
    if Function in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F10", "F11", "F12", "F13", "F14", "F18"]:
        dataframe = dataframe.round(1)
    elif Function in ["F17"]:
        dataframe = dataframe.round(3)
    elif Function in ["F19","F20"]:
        dataframe = dataframe.round(2)
    elif Function in ["F8","F15","F16","F21","F22","F23"]:
        dataframe = dataframe.round(4)

    # display(dataframe,optimal)
    dataframe = pd.DataFrame(data=dataframe.values,
                             columns=dataframe.columns)
    percent_dataframe = dataframe.applymap(lambda x: True if x == optimal else False)
    # display(percent_dataframe)
    percent_dataframe["Function"] = Function
    return percent_dataframe


# function_list = np.arange(1, 24, 1)
function_list = [2,4,5,7]
percent_df = [percent(Function="F" + str(i), optimal=opt[i-1]) for i in function_list]
percent_df = pd.concat(percent_df, axis=0)
percent_df = percent_df.groupby(["Function"]).sum().applymap(lambda x: str(x * 10) + "%")
index = ["F"+str(i) for i in function_list]
percent_df = percent_df.loc[index]
display(percent_df)
percent_df.to_csv("./Larmack121_percent_f2_4_5_7_1000000_50d.csv")
