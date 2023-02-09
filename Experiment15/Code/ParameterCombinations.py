# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 2/9/23 10:35
import pandas as pd


def generate_parameter_combinations():
    gg = [0.01, 0.2, 0.5, 0.8, 0.99]
    selection_method = ["SSGA", "sorted_selection_part", "sorted_selection_all", "roulette_Wheel_Select"]
    fitness_function = [1, 5, 7, 8, 10, 13]
    algorithm = ["Baseline", "Lamarck", "Baldwin"]
    rest_parameters = []
    for generation_gap in gg:
        for selection in selection_method:
            for func in fitness_function:
                for algo in algorithm:
                    rest_parameters.append([generation_gap, selection, func, algo])
    fixed_parameters = pd.read_csv("fixed_parameters.csv", header=0, index_col=[0])
    fixed_parameters_columns = fixed_parameters.columns.tolist()
    fixed_parameters = fixed_parameters.values.tolist()
    parameter_combinations = []
    for i in range(len(fixed_parameters)):
        for j in range(len(rest_parameters)):
            parameter_combinations.append(fixed_parameters[i] + rest_parameters[j])
    parameter_combinations = pd.DataFrame(parameter_combinations)
    parameter_combinations.columns = fixed_parameters_columns + ["gg", "selection_method", "fitness_function",
                                                                 "algorithm"]
    return parameter_combinations


