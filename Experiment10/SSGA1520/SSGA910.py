# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/12/22 14:42

import time
from parameter_combination import read_file
import pandas as pd

import improved_evolution

if __name__ == '__main__':
    opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
           -10.4028, -10.5363]

    com_df = pd.read_csv("./best_20_pm.csv",
                         index_col=[0],
                         header=0)
    com_df["R"] = 0.1
    df_col = com_df.columns.tolist()
    df_col.remove("range_mutation")
    print([df_col])
    com_df = com_df[df_col]
    com_df.to_csv("./best_20com_9pm.csv", header=True, index=True)
    data_pm = pd.read_csv("./best_20com_9pm.csv", header=0, index_col=[0])

    com = data_pm.values.tolist()[8:10]
    index = data_pm.index.tolist()[8:10]

    function_list = [15,20]

    for i in range(0, len(com), 1):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if i % 5 == 4:
            print("\033[0;37;45m {0} combinations are tested.\033[0m".format(i + 1))
        data, data_budget,data_similarity = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
                                                         function_list=function_list)
        data.to_csv("./combination{0}.csv".format(index[i]), header=True, index=True)
        data_budget.to_csv("./budget{0}.csv".format(index[i]), header=True, index=True)
        data_similarity.to_csv("./similarity{0}.csv".format(index[i]), header=True, index=True)

