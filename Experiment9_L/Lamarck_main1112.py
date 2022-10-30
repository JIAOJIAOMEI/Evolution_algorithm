# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 16:00
import time

import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
import improved_evolution
from parameter_combination import read_file

if __name__ == '__main__':
    opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.0003, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
           -10.4028, -10.5363]

    com_df = pd.read_csv("./best_20_pm.csv",
                         index_col=[0],
                         header=0)
    com_df["L"] = 1
    com_df["K"] = 1
    com_df["R"] = 0.01  # 0.05

    df_col = com_df.columns.tolist()
    df_col.remove("range_mutation")
    print([df_col])
    com_df = com_df[df_col]
    com_df.to_csv("./best_20com_9pm.csv", header=True, index=True)
    data_pm = pd.read_csv("./best_20com_9pm.csv", header=0, index_col=[0])
    com = data_pm.values.tolist()[10:12]
    index = data_pm.index.tolist()[10:12]
    print(com, index)

    function_list = [i for i in range(1, 24, 1)]

    for i in range(0, len(com), 1):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        data, data_budget, data_similarity = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
                                                                          mode="Lamarck",
                                                                          function_list=function_list)
        data.to_csv("./combination{0}.csv".format(index[i]), header=True, index=True)
        data_budget.to_csv("./budget{0}.csv".format(index[i]), header=True, index=True)
        data_similarity.to_csv("./similarity{0}.csv".format(index[i]), header=True, index=True)
