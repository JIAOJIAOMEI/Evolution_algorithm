# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/18/22 01:03
import time

import numpy as np
import pandas as pd
from IPython.core.display_functions import display

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
com_df = pd.read_csv("./best_combination_new.csv",
                     index_col=[0],
                     header=0)
com = com_df.values.tolist()
index = com_df.index.tolist()

# display(com_df.nunique(axis=0))
sheet_name = ["combination" + str(i) for i in index]
opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
       -10.4028, -10.5363]


def read_file(sheetname, path):
    df = pd.read_excel(path, sheet_name=sheetname,
                       header=0,
                       index_col=[0, 1])
    df = df.rename_axis(["Function", "Times"])
    return df

path=["Baseline_table_short_best_combination_500.xlsx",
      "Baseline_table_short_best_combination_2000.xlsx",
      "Baseline_table_short_best_combination_5000.xlsx",
      "Baseline_table_short_best_combination_30000.xlsx"]
iterations =[500,2000,5000,30000]

with pd.ExcelWriter("Number.xlsx") as writer:
    for i,pathname in enumerate(path):
        data = [read_file(name,pathname) for name in sheet_name]
        data = pd.concat(data, axis=1)
        data.columns = sheet_name
        data.to_excel(writer, sheet_name=str(iterations[i]))

path3="Number.xlsx"
data = [read_file(str(name),path3) for name in iterations]
data = pd.concat(data, axis=0,keys=[500,2000,5000,30000])
data = data.rename_axis(["iterations","Function", "Times"])
data.columns = sheet_name
data = data.unstack(level=0)
data.to_csv("./Number.csv")

