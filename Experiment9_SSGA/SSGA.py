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
    com_df["R"] = 0.01
    df_col = com_df.columns.tolist()
    df_col.remove("range_mutation")
    print([df_col])
    com_df = com_df[df_col]
    com_df.to_csv("./best_20com_9pm.csv", header=True, index=True)
    data_pm = pd.read_csv("./best_20com_9pm.csv", header=0, index_col=[0])

    com = data_pm.values.tolist()[2:3]
    index = data_pm.index.tolist()[2:3]
    # print(data_pm)


    #
    # function_list = [i for i in range(1, 24, 1)]
    # function_list =[1,2,3,4,5,6,7,9,10,11,12,13,14,18]  # round(0)
    function_list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # round(0)
    # function_list = [17] # round(3)
    # function_list = [8,19,20] # round(2)
    # function_list = [15,16,21,22,23] # round(4)
    # function_list = [17] # test
    print(len(function_list))
    #

    for i in range(0, len(com), 1):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if i % 5 == 4:
            print("\033[0;37;45m {0} combinations are tested.\033[0m".format(i + 1))
        data, temp = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i],
                                                  function_list=function_list)

    #
    # sheet_name = ["combination" + str(i) for i in index]
    # path = "SSGA.xlsx"
    # df = [read_file(name, path) for name in sheet_name]
    # df = pd.concat(df, axis=1)
    # df.columns = sheet_name
    # df.to_csv("./SSGA.csv")
