# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 16:00
import time

import pandas as pd

# 显示所有列
# pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
import improved_evolution
from parameter_combination import read_file

if __name__ == '__main__':
    dim=100
    opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * dim, 0, 0, 0, 0, 0, 1, 0.0003, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
           -10.4028, -10.5363]

    com_df = pd.read_csv("./best_20_pm.csv",
                         index_col=[0],
                         header=0)
    com_df["local_search_rate"] = 0.2
    com_df["Local_search_type"] = "Uniform"
    com_df["R"] = 0.01
    df_col = com_df.columns.tolist()
    df_col.remove("range_mutation")
    print(f"col names are {[df_col]}")
    com_df = com_df[df_col]
    com_df.to_csv("./best_20com_9pm.csv", header=True, index=True)
    data_pm = pd.read_csv("./best_20com_9pm.csv", header=0, index_col=[0])
    com = data_pm.values.tolist()
    index = data_pm.index.tolist()
    print(data_pm, com, index)
    data_pm = data_pm.drop_duplicates()
    data_pm.to_csv("./best_20com_9pm_inuse.csv", header=True, index=True)
    com = data_pm.values.tolist()[0:2]
    index = data_pm.index.tolist()[0:2]
    print(data_pm, com, index)

    function_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    for i in range(0, len(com), 1):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        data, data_budget, data_similarity = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
                                                                          mode="Lamarck",
                                                                          function_list=function_list)
        data.to_csv("./combination{0}.csv".format(index[i]), header=True, index=True)
        data_budget.to_csv("./budget{0}.csv".format(index[i]), header=True, index=True)
        data_similarity.to_csv("./similarity{0}.csv".format(index[i]), header=True, index=True)
