# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/16/22 19:21
from collections import Counter

import numpy as np
import pandas as pd
from IPython.core.display_functions import display

lst1 = [[146, 164, 163, 162, 145, 199, 182, 144, 180, 181, 198, 23, 5, 22, 77, 59, 41, 95, 4, 21],
        [199, 56, 163, 36, 108, 91, 92, 126, 198, 59, 95, 23, 22, 131, 57, 94, 98, 130, 113, 80],
        [187, 191, 189, 129, 188, 186, 169, 168, 171, 172, 190, 93, 154, 155, 192, 22, 31, 115, 24, 134]]
lst2 = [[110, 128, 146, 164, 145, 163, 182, 144, 162, 199, 181, 198, 180, 23, 59, 22, 5, 95, 41, 58],
        [145, 128, 110, 146, 164, 163, 182, 199, 144, 162, 181, 198, 180, 23, 59, 41, 21, 5, 95, 58],
        [16, 17, 179, 89, 35, 69, 178, 53, 143, 125, 51, 52, 88, 197, 70, 160, 161, 105, 33, 123]]

lst = lst1 + lst2
lst = np.array(lst).reshape(-1)
count = Counter(lst)
display(count.most_common(20))


def splitListOfTuples(lst):
    lst1 = []
    lst2 = []
    for x, y in lst:
        lst1.append(x)
        lst2.append(y)
    return (lst1, lst2)


key, value = splitListOfTuples(count.most_common(20))
display(key, type(key))

com_file = "/Users/meijiaojiao/Desktop/Evolution_algorithm/Baseline_f3_f6_f12/Linear_combination_crossover_normal/combinations_result_baseline.csv"
df_com = pd.read_csv(com_file, header=0)
# display(df_com)

com = [df_com.loc[i] for i in key]
df = pd.DataFrame(data=com)

df.to_csv('./best_combination_new.csv',
          sep=',',
          header=True,
          index=True)
# display(df)

df = pd.read_csv("./best_combination_new.csv",
                 index_col=[0],
                 header=0)
# display(df)
com = df.values.tolist()
display(com)
