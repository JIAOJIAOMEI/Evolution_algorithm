# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/9/22 18:40
import pandas as pd
from IPython.core.display_functions import display

com_file = "./Linear_combination_crossover_normal/combinations_result_baseline.csv"
df_com = pd.read_csv(com_file, header=0)
df_com = df_com[:200]

file_name = ["Linear_combination_crossover_normal",
             "Linear_combination_crossover_uniform",
             "Probabilistic_crossover_normal",
             "Probabilistic_crossover_uniform",
             "singe_point_crossover_normal",
             "singe_point_crossover_uniform"]


def com_200(filename):
    com_df_label = df_com.copy()
    com_df_label.index = [i for i in range(1, len(com_df_label) + 1)]
    if filename == "Linear_combination_crossover_normal":
        print("1")
        com_df_label["Mutation_type"] = "Normal"
        com_df_label["Crossover_type"] = "Linear_combination_crossover"

    elif filename == "Linear_combination_crossover_uniform":
        print("2")
        com_df_label["Mutation_type"] = "Uniform"
        com_df_label["Crossover_type"] = "Linear_combination_crossover"

    elif filename == "Probabilistic_crossover_normal":
        print("3")
        com_df_label["Mutation_type"] = "Normal"
        com_df_label["Crossover_type"] = "Probabilistic_crossover"

    elif filename == "Probabilistic_crossover_uniform":
        print("4")
        com_df_label["Mutation_type"] = "Uniform"
        com_df_label["Crossover_type"] = "Probabilistic_crossover"

    elif filename == "singe_point_crossover_normal":
        print("5")
        com_df_label["Mutation_type"] = "Normal"
        com_df_label["Crossover_type"] = "Singe_point_crossover"

    elif filename == "singe_point_crossover_uniform":
        print("6")
        com_df_label["Mutation_type"] = "Uniform"
        com_df_label["Crossover_type"] = "Singe_point_crossover"
    display(com_df_label)

    return com_df_label


combine_comdf = [com_200(name) for name in file_name]
combine_comdf = pd.concat(combine_comdf,axis=0)
combine_comdf.index = [i for i in range(1,len(combine_comdf)+1)]
display(combine_comdf)

combine_comdf.to_csv("./parameter_combination_1200.csv",
                     index=True,
                     header=True)