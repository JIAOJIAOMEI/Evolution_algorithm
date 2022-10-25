# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 16:00
import time

import pandas as pd
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
import improved_evolution
from parameter_combination import read_file

if __name__ == '__main__':
    opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
           -10.4028, -10.5363]

    com_df = pd.read_csv("./best_20_pm.csv",
                         index_col=[0],
                         header=0)
    com_df["L"] = 5
    com_df["K"] = 1
    com_df["deltah"] = 0.5
    print(com_df)
    com = com_df.values.tolist()
    index = com_df.index.tolist()

    # function_list = [i for i in range(1, 24, 1)]
    #
    # # for i in range(0, len(com), 1):
    # #     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # #     data,data_budget = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
    # #                                                                         mode="Baldwin",
    # #                                                                         function_list=function_list)
    # #     data.to_csv("./combination{0}.csv".format(index[i]),header=True,index=True)
    # #     data_budget.to_csv("./budget{0}.csv".format(index[i]),header=True,index=True)
    #
    with pd.ExcelWriter("Baldwin.xlsx") as writer:
        for i in range(0, len(com), 1):
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            data, data_budget = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
                                                             mode="Baldwin",
                                                             function_list=[18])
            data.to_excel(writer, sheet_name="combination" + str(index[i]))
            data_budget.to_excel(writer, sheet_name="budget" + str(index[i]))