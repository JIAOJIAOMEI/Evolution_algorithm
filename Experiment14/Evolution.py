# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/2/23 00:32
from FunctionsParameter import get_functions_parameter


# create a class to store the information of algorithm parameters

class AlgorithmParameters:
    def __init__(self, num_generations, mutation_rate, num_individuals, crossover_rate, mutation_type, crossover_type,
                 local_search_rate, local_search_type, search_radius, num_evaluations, fitness_function, dimensions,
                 algorithm):
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.num_individuals = num_individuals
        self.crossover_rate = crossover_rate
        self.mutation_type = mutation_type
        self.crossover_type = crossover_type
        self.local_search_rate = local_search_rate
        self.local_search_type = local_search_type
        self.search_radius = search_radius
        self.num_evaluations = num_evaluations
        func, num_genes, genotype_range = get_functions_parameter(fitness_function, flexible_dimensions=dimensions)
        self.func = func
        self.num_genes = num_genes
        self.genotype_range = genotype_range
        if algorithm == "Baseline":
            self.local_search_type = "None"
            self.local_search_rate = "None"


import pandas as pd
import numpy as np
import random


# create a function to generate parameter combinations using each parameter from above
# and store it in a dataframe, each row is a combination of parameters
def generate_parameter_combinations():
    num_generations = [1000, 10000]
    mutation_rate = [0.05, 0.1]
    num_individuals = [200]
    crossover_rate = [0.5, 0.9]
    mutation_type = ["uniform", "gaussian", "frequency_based"]
    crossover_type = ["one-point", "two-point", "probabilistic", "linear combination", "average", "Roulette wheel"]
    local_search_rate = [0.1, 0.5]
    local_search_type = ["uniform", "gaussian", "hill climbing"]
    search_radius = [0.005, 0.01, 0.05, 0.1]
    num_evaluations = [10000, 50000]
    fitness_function = [i for i in range(1, 14)]
    dimensions = [50, 100, 200, 400]
    parameter_combinations = []
    for i in num_generations:
        for j in mutation_rate:
            for k in num_individuals:
                for l in crossover_rate:
                    for m in mutation_type:
                        for n in crossover_type:
                            for o in local_search_rate:
                                for p in local_search_type:
                                    for q in search_radius:
                                        for r in num_evaluations:
                                            for s in fitness_function:
                                                for t in dimensions:
                                                    parameter_combinations.append(
                                                        [i, j, k, l, m, n, o, p, q, r, s, t])
    parameter_combinations = pd.DataFrame(parameter_combinations,
                                          columns=["num_generations", "mutation_rate", "num_individuals",
                                                   "crossover_rate",
                                                   "mutation_type", "crossover_type", "local_search_rate",
                                                   "local_search_type", "search_radius", "num_evaluations",
                                                   "fitness_function", "dimensions"])
    # save the dataframe to a csv file
    parameter_combinations.to_csv("parameter_combinations.csv", index=True)
    return parameter_combinations


# parameter_combinations = generate_parameter_combinations()
dataframe = pd.read_csv("parameter_combinations.csv", header=0, index_col=0)
num_rows, num_columns = dataframe.shape
for i in range(num_rows):
    parameter_combination = dataframe.iloc[i, :]
    # simply the following code
    algorithm_parameters = AlgorithmParameters(parameter_combination[0], parameter_combination[1],
                                               parameter_combination[2], parameter_combination[3],
                                               parameter_combination[4], parameter_combination[5],
                                               parameter_combination[6], parameter_combination[7],
                                               parameter_combination[8], parameter_combination[9],
                                               parameter_combination[10], parameter_combination[11], "Baseline")


# define a function, evolution_loop, to run the algorithm
