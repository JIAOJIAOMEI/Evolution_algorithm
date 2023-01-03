# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/3/23 18:30
from Evolution import evolution_loop
from FunctionsParameter import get_functions_parameter
import pandas as pd


# create a class to store the information of algorithm parameters
class AlgorithmParameters:
    def __init__(self, num_generations, mutation_rate, num_individuals, crossover_rate, mutation_type, crossover_type,
                 local_search_rate, local_search_type, search_radius, num_evaluations, fitness_function, dimensions,
                 algorithm, gg, selection_method):
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
            self.local_search_type = None
            self.local_search_rate = None
        self.gg = gg
        self.selection_method = selection_method
        self.algorithm = algorithm


# create a function to generate parameter combinations using each parameter from above
# and store it in a dataframe, each row is a combination of parameters
def generate_parameter_combinations():
    num_generations = [20]
    mutation_rate = [0.5]
    num_individuals = [10]
    crossover_rate = [0.5]
    mutation_type = ["uniform"]  # "uniform", "gaussian", "frequency_based"
    crossover_type = ["one-point","two-point", "probabilistic", "linear combination", "average", "Roulette wheel"]  # "two-point", "probabilistic", "linear combination", "average", "Roulette wheel"
    local_search_rate = [0.5]
    local_search_type = ["uniform"]  # "uniform", "gaussian", "hill climbing"
    search_radius = [0.1]
    num_evaluations = [3000]
    fitness_function = [1]
    dimensions = [5]
    algorithm = ["Baseline"]  # , "Lamarck", "Baldwin"
    gg = [0.5]
    selection_method = [
        "best_and_worst"]  # "best_and_worst", "sorted_selection_part", "sorted_selection_all", "roulette_Wheel_Select"
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
                                                    for u in algorithm:
                                                        for v in gg:
                                                            for w in selection_method:
                                                                parameter_combinations.append(
                                                                    [i, j, k, l, m, n, o, p, q, r, s, t, u, v, w])
    parameter_combinations = pd.DataFrame(parameter_combinations,
                                          columns=["num_generations", "mutation_rate", "num_individuals",
                                                   "crossover_rate", "mutation_type", "crossover_type",
                                                   "local_search_rate", "local_search_type", "search_radius",
                                                   "num_evaluations", "fitness_function", "dimensions",
                                                   "algorithm", "gg", "selection_method"])
    # save the dataframe to a csv file
    parameter_combinations.to_csv("parameter_combinations.csv", index=True)
    return parameter_combinations


import colorama

parameter_combinations = generate_parameter_combinations()
dataframe = pd.read_csv("parameter_combinations.csv", header=0, index_col=0)
num_rows, num_columns = dataframe.shape
solutions = []
for i in range(num_rows):
    # create a list to store the final solution of each run
    parameter_combination = dataframe.iloc[i, :]
    print(colorama.Fore.GREEN + "The parameter combination is:\n" + str(parameter_combination))
    # simply the following code
    algorithm_parameters = AlgorithmParameters(parameter_combination[0], parameter_combination[1],
                                               parameter_combination[2], parameter_combination[3],
                                               parameter_combination[4], parameter_combination[5],
                                               parameter_combination[6], parameter_combination[7],
                                               parameter_combination[8], parameter_combination[9],
                                               parameter_combination[10], parameter_combination[11],
                                               parameter_combination[12], parameter_combination[13],
                                               parameter_combination[14])
    # create a list to store the final solution of multiple runs
    num_runs = 1
    final_solutions = []
    for run in range(num_runs):
        final_solutions.append(evolution_loop(algorithm_parameters))
    solutions.append(final_solutions)
    # index is the index of the parameter combination
    # columns are the runs
    # the value is the final solution of the run
    # create a dataframe to store the final solutions
    solutions_dataframe = pd.DataFrame(solutions)
    # save the dataframe to a csv file
    solutions_dataframe.to_csv("solutions_dataframe.csv", index=True)
