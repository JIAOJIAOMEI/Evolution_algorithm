# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/9/22 17:45

import numpy as np
import pandas as pd
from IPython.core.display_functions import display

f_list = ["F" + str(i) for i in [1, 3, 6, 12, 18, 22]]


def read_df(function):
    path = "./" + function + ".csv"
    df = pd.read_csv(path, header=[0], index_col=0)
    # display(function,df.shape,df)
    # df.loc["sum"] = df.sum(axis=0)
    # display(df.loc["sum"])
    # return df.loc["sum"]
    df = df.T
    display(df)
    return df


data = [read_df(function) for function in f_list]
data = pd.concat(data,axis=0)
display(data.shape,data)
display(data.columns)
data.loc["sum"] = data.sum(axis=0)
dataframe = data.sort_values(by="sum", axis=1, ascending=True, na_position="last")
display(dataframe)
# display(dataframe.columns)
k = dataframe.columns.tolist()[:20]
display(k)

pm_1200 = pd.read_csv("./parameter_combination_1200.csv",
                      index_col=[0],
                      header=0)
# display(pm_1200)

best_20_frame= pm_1200.loc[k]
display(best_20_frame)
best_20_frame.to_csv("./best_20_pm.csv",
                     index=True,
                     header=True)
# df1 = pd.DataFrame(
#           {'num': [1, 2],
#            'char': ['a', 'b']})
# df2 = pd.DataFrame(
#           {'char': ['b', 'c'],
#            'num': [3, 4]})
# display(df1)
# display(df2)
# display(pd.concat([df1,df2],axis=0))
