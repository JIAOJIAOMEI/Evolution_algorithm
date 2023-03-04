# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 2/9/23 10:35
import pandas as pd


# This function is used to generate the parameter combinations for the experiments
def generate_parameter_combinations():
    length_of_local_search = [1]
    redo_local_search_rate = [0]
    fitness_function = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23] # multimodal functions
    algorithm = ["Baseline", "Lamarck", "Baldwin"]
    rest_parameters = []

    for length in length_of_local_search:
        for redo in redo_local_search_rate:
            for func in fitness_function:
                for algo in algorithm:
                    rest_parameters.append([length, redo, func, algo])

    fixed_parameters = pd.read_csv("pm.csv", header=0,
                                   index_col=[0])  # this csv could be changed
    # drop last four columns
    print(fixed_parameters.columns.tolist())
    fixed_parameters = fixed_parameters.iloc[:, :-4]
    print(fixed_parameters.columns.tolist())
    # change crossover_rate to 0.7
    fixed_parameters["crossover_rate"] = 0.7
    # change mutation_rate to 0.03
    fixed_parameters["mutation_rate"] = 0.03
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
    parameter_combinations.columns = fixed_parameters_columns + ["length_of_local_search", "redo_local_search_rate",
                                                                 "fitness_function",
                                                                 "algorithm"]
    print(parameter_combinations.columns.tolist())
    # parameter_combinations.to_csv("parameter_combinations.csv", index=True)
    return parameter_combinations


# generate_parameter_combinations()
