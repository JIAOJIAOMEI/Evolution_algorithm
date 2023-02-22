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
                 algorithm, gg, selection_method, threshold, length_of_local_search):
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
        self.length_of_local_search = length_of_local_search
        func, num_genes, genotype_range = get_functions_parameter(fitness_function, flexible_dimensions=dimensions)
        self.func = func
        self.num_genes = num_genes
        self.genotype_range = genotype_range
        if algorithm == "Baseline":
            self.local_search_type = None
            self.local_search_rate = None
            self.length_of_local_search = None
        self.gg = gg
        self.selection_method = selection_method
        self.algorithm = algorithm
        self.threshold = threshold


# create a function to generate parameter combinations using each parameter from above
# and store it in a dataframe, each row is a combination of parameters
from ParameterCombinations import generate_parameter_combinations
parameter_combinations = generate_parameter_combinations()
parameter_combinations.to_csv("parameter_combinations.csv")

import colorama
# count time for the whole program
import time
from datetime import datetime


dataframe = pd.read_csv("parameter_combinations.csv", header=0, index_col=0)
num_rows, num_columns = dataframe.shape
print("The number of parameter combinations is: " + str(num_rows))
solutions = []
start_time = datetime.now()
print(f"start time is {start_time}")
for i in range(1):
    if i % 100 == 0:
        print("The number of parameter combinations that have been tested is: " + str(i))
        print(datetime.now())
    # create a list to store the final solution of each run
    parameter_combination = dataframe.iloc[i, :]
    # print(colorama.Fore.GREEN + "The parameter combination is:\n" + str(parameter_combination))
    # simply the following code
    algorithm_parameters = AlgorithmParameters(num_generations=parameter_combination["num_generations"],
                                               mutation_rate=parameter_combination["mutation_rate"],
                                               num_individuals=parameter_combination["num_individuals"],
                                               crossover_rate=parameter_combination["crossover_rate"],
                                               mutation_type=parameter_combination["mutation_type"],
                                               crossover_type=parameter_combination["crossover_type"],
                                               local_search_rate=parameter_combination["local_search_rate"],
                                               local_search_type=parameter_combination["local_search_type"],
                                               search_radius=parameter_combination["search_radius"],
                                               threshold=parameter_combination["threshold"],
                                               gg=parameter_combination["gg"],
                                               dimensions=parameter_combination["dimensions"],
                                               num_evaluations=parameter_combination['dimensions'] * 10000,
                                               selection_method=parameter_combination["selection_method"],
                                               fitness_function=parameter_combination["fitness_function"],
                                               algorithm=parameter_combination["algorithm"],
                                               length_of_local_search=parameter_combination["length_of_local_search"])
    # create a list to store the final solution of multiple runs
    num_runs = 10
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

end_time = datetime.now()
print('The total time is: {}'.format(end_time - start_time))
