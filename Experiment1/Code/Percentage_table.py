# Name: Mei Jiaojiao
# Specilization: Artificial Intelligence
# Time and date: 7/28/22 12:48

import pandas as pd
from IPython.core.display_functions import display

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None


# Baldwin = pd.read_csv(
#     "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/Long_format_table/Baldwin_table_long_1_3072.csv",
#     index_col=[0, 1], header=0, sep=",")
# Baldwin.columns = [i for i in range(1, 3073, 1)]

Lamarck = pd.read_csv(
    "Lamarck_table_long_1_3072.csv",
    index_col=[0, 1], header=0, sep=",")
Lamarck.columns = [i for i in range(1, 3073, 1)]


k = ["F" + str(i) for i in range(1, 24, 1)]
h = k
opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
       -10.4028, -10.5363]
for i in range(0, 23):
    h[i] = Lamarck.loc[k[i]].copy()
    h[i].round(4)
    h[i] = h[i].applymap(lambda x: 1 if x <= opt[i] else 0)
    h[i].loc["SUM"] = h[i].apply(lambda x: x.sum())
df = pd.concat(h, keys=(
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18',
    'F19', 'F20', 'F21', 'F22', 'F23'))

result = df.swaplevel().loc['SUM']
result = result.applymap(lambda x: str(x * 10) + "%")
result.to_csv('Lamarck_percentage_table.csv',
              sep=',',
              header=True,
              index=True)
