# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 16:00
import numpy as np

import improved_evolution
import parameter_combination

if __name__ == '__main__':
    parameter_combination.combination()
    com = parameter_combination.read_com()

    # data, short_data, temp = improved_evolution.multiple(mode="Lamarck", Times=10, L=[0, len(com)], Com=com)
    data, short_data, temp = improved_evolution.multiplef(mode="Lamarck", Times=7, L=[0, len(com)], Com=com,
                                                          function_list=[22])
    with open("Lamarck_3Dlist_short.txt", "w") as w:
        w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
    with open("Lamarck_3Dlist_long.txt", "w") as w:
        w.write(np.array2string(temp))
    short_data.to_csv('./Lamarck_table_short.csv',
                      sep=',',
                      header=True,
                      index=True)
    data.to_csv('./Lamarck_table_long.csv',
                sep=',',
                header=True,
                index=True)
