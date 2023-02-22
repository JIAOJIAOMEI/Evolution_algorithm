# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 2/9/23 10:35
import pandas as pd


# This function is used to generate the parameter combinations for the experiments
def generate_parameter_combinations():

    length_of_local_search = [3]
    fitness_function = [1, 5, 7, 8, 10, 13]
    algorithm = ["Baseline", "Lamarck", "Baldwin"]
    rest_parameters = []

    for length in length_of_local_search:
        for func in fitness_function:
            for algo in algorithm:
                rest_parameters.append([length, func, algo])

    fixed_parameters = pd.read_csv("best_20_baseline_experiment15.csv", header=0,
                                   index_col=[0])  # this csv could be changed
    # it contains good parameters selected based on previous experiments
    # this generation_parameters.py is used to generate the parameters for some new parameters
    # drop the columns algorithm
    fixed_parameters = fixed_parameters.drop(["algorithm"], axis=1)  # this list could be changed
    fixed_parameters_columns = fixed_parameters.columns.tolist()
    fixed_parameters = fixed_parameters.values.tolist()
    parameter_combinations = []
    for i in range(len(fixed_parameters)):
        for j in range(len(rest_parameters)):
            parameter_combinations.append(fixed_parameters[i] + rest_parameters[j])
    parameter_combinations = pd.DataFrame(parameter_combinations)
    parameter_combinations.columns = fixed_parameters_columns + ["length_of_local_search", "fitness_function",
                                                                 "algorithm"]

    return parameter_combinations
