# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 16:00
import time

import pandas as pd

import improved_evolution
from parameter_combination import read_file

if __name__ == '__main__':
    opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532,
           -10.4028, -10.5363]
    # parameter_combination.combination()
    # com_df = parameter_combination.read_com()
    com_df = pd.read_csv("./best_20_pm.csv",
                         index_col=[0],
                         header=0)
    com_df["num_phenotypes"] = 5
    print(com_df)
    com = com_df.values.tolist()[16:18]
    index = com_df.index.tolist()[16:18]
     
    function_list = [i for i in range(1, 24, 1)]

    with pd.ExcelWriter("Baldwin1617.xlsx") as writer:
        for i in range(0, len(com), 1):
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            # if i % 5 == 4:
            #     print("\033[0;37;45m {0} combinations are tested.\033[0m".format(i + 1))
            data, temp = improved_evolution.multipleF(Times=10, L=[0, 1], Com=com[i], mode="Baldwin",
                                                      function_list=function_list)
            data.to_excel(writer, sheet_name="combination" + str(index[i]))

    sheet_name = ["combination" + str(i) for i in index]
    path = "Baldwin1617.xlsx"
    df = [read_file(name, path) for name in sheet_name]
    df = pd.concat(df, axis=1)
    df.columns = sheet_name
    df.to_csv("./Baldwin1617.csv")
