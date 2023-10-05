# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 2/9/23 10:35
import pandas as pd


# This function is used to generate the parameter combinations for the experiments
def generate_parameter_combinations():
    fitness_function = [21]
    algorithm = ["Baseline", "Lamarck", "Baldwin"]
    rest_parameters = []

    for func in fitness_function:
        for algo in algorithm:
            rest_parameters.append([func, algo])

    fixed_parameters = pd.read_csv("pm_table.csv", header=0,
                                   index_col=[0])  # this csv could be changed

    # get unique rows
    fixed_parameters = fixed_parameters.drop_duplicates()
    # shape of fixed_parameters is
    print(fixed_parameters.shape)
    fixed_parameters_columns = fixed_parameters.columns.tolist()
    fixed_parameters = fixed_parameters.values.tolist()
    parameter_combinations = []
    for i in range(len(fixed_parameters)):
        for j in range(len(rest_parameters)):
            parameter_combinations.append(fixed_parameters[i] + rest_parameters[j])
    parameter_combinations = pd.DataFrame(parameter_combinations)
    parameter_combinations.columns = fixed_parameters_columns + ["fitness_function", "algorithm"]
    print(parameter_combinations.columns.tolist())
    # parameter_combinations.to_csv("parameter_combinations.csv", index=True)
    return parameter_combinations


# generate_parameter_combinations()
