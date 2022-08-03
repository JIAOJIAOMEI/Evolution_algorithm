# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/1/22 14:30

import itertools
import random
import statistics
import sys

import numpy as np
import pandas as pd

import improved_fitness_functions

pd.options.display.max_columns = None
pd.options.display.max_rows = None

np.set_printoptions(threshold=sys.maxsize)

'''The class Individual is to generate genotype and generate phenotype ===== genotype.'''


class Individual:
    def __init__(self, genotype, num_genes, genotype_range, pattern):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.phenotype = self.genotype
        elif pattern == 1:
            self.genotype = genotype
            self.phenotype = self.genotype


''' This fitness function is to calculate the fitness values for a group number of individuals.
or in other words, to calculate the first generation(first iteration)'''


def fitness(individuals, func):
    fit = []
    for individual in individuals:
        fit.append(func(individual.phenotype))
    best_fit = np.argmin(fit)
    worst_fit = np.argmax(fit)
    return best_fit, worst_fit, fit


''' This fitness_single function is to calculate the fitness value for the new individual from the second iteration'''


def fitness_single(individual, func):
    return func(individual.phenotype)


''' This offspring function is to do crossover and mutation.
first we need to know the mode, if it is "Lamarck", then we generate offspring using phenotype, 
                                if it is "Baldwin", then we generate offspring using genotype,
second, delete the worst one,
third, choose a random individual and do crossover with the best one,
fourth, choose a random result between the two results obtained by crossover,
fifth, based on the crossover result, do mutation, the operation is the same as local search
the location for crossover is randomly chosen each time.'''


def offspring(individuals, num_genes, best_fit, worst_fit, mutation_rate, range_mutation, crossover_probability,
              mutation_type, crossover_type):
    n = []
    for individual in individuals:
        n.append(individual.phenotype)
    result = []
    if crossover_type == 0:  # Probabilistic crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        partner_index = np.random.randint(0, len(n))
        parent2 = n[partner_index]
        for j in range(len(parent1)):
            if np.random.rand() < crossover_probability:
                result.append(parent1[j])
            else:
                result.append(parent2[j])
    elif crossover_type == 1:  # singe-point-crossover
        if np.random.rand() < crossover_probability:
            cross_location = np.random.randint(0, num_genes)
            part1 = n[best_fit][:cross_location]
            part2 = n[best_fit][cross_location:]
            del n[worst_fit]
            partner_index = np.random.randint(0, len(n))
            pindex_part1 = n[partner_index][:cross_location]
            pindex_part2 = n[partner_index][cross_location:]
            result1 = list(itertools.chain(pindex_part1, part2))
            result2 = list(itertools.chain(part1, pindex_part2))
            result = random.choice([result1, result2])
        else:
            result1 = n[best_fit]
            del n[worst_fit]
            result2_index = np.random.randint(0, len(n))
            result2 = n[result2_index]
            result = random.choice([result1, result2])
    elif crossover_type == 2:  # Linear combination crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        partner_index = np.random.randint(0, len(n))
        parent2 = n[partner_index]
        for j in range(len(parent1)):
            new_j = parent1[j] * crossover_probability + parent2[j] * (1 - crossover_probability)
            result.append(new_j)
    # numpy.random.rand from uniform (in range [0,1))
    # numpy.random.normal generates samples from the normal distribution
    mutation_rate = mutation_rate / num_genes
    if mutation_type == 0:
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + np.random.uniform(-range_mutation, range_mutation)
    elif mutation_type == 1:
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + float(
                    np.random.normal(loc=0, scale=2 * range_mutation, size=1) - range_mutation)
    return result


'''This initialization function is to generate the initial group
for each individual in the group, generate the genotype and the phenotype'''


def initialization(num_genes, num_individual, genotype_range):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(
            Individual(num_genes=num_genes, genotype=None, genotype_range=genotype_range, pattern=0))
    return individuals


'''This choose_func function is to choose a specific function,
each function has its own dimensions(num_genes) and genotype_range'''


def choose_func(function):
    func = None
    num_genes = None
    genotype_range = None
    if function == 1:
        func = improved_fitness_functions.F1
        num_genes = 10
        genotype_range = [-100, 100]
    elif function == 2:
        func = improved_fitness_functions.F2
        num_genes = 10
        genotype_range = [-100, 100]
    elif function == 3:
        func = improved_fitness_functions.F3
        num_genes = 10
        genotype_range = [-100, 100]
    elif function == 4:
        func = improved_fitness_functions.F4
        num_genes = 10
        genotype_range = [-100, 100]
    elif function == 5:
        func = improved_fitness_functions.F5
        num_genes = 10
        genotype_range = [-30, 30]
    elif function == 6:
        func = improved_fitness_functions.F6
        num_genes = 10
        genotype_range = [-100, 100]
    elif function == 7:
        func = improved_fitness_functions.F7
        num_genes = 10
        genotype_range = [-1.28, 1.28]
    elif function == 8:
        func = improved_fitness_functions.F8
        num_genes = 10
        genotype_range = [-500, 500]
    elif function == 9:
        func = improved_fitness_functions.F9
        num_genes = 10
        genotype_range = [-5.12, 5.12]
    elif function == 10:
        func = improved_fitness_functions.F10
        num_genes = 10
        genotype_range = [-32, 32]
    elif function == 11:
        func = improved_fitness_functions.F11
        num_genes = 10
        genotype_range = [-600, 600]
    elif function == 12:
        func = improved_fitness_functions.F12
        num_genes = 10
        genotype_range = [-50, 50]
    elif function == 13:
        func = improved_fitness_functions.F13
        num_genes = 10
        genotype_range = [-50, 50]
    elif function == 14:
        func = improved_fitness_functions.F14
        num_genes = 2
        genotype_range = [-65, 65]
    elif function == 15:
        func = improved_fitness_functions.F15
        num_genes = 4
        genotype_range = [-5, 5]
    elif function == 16:
        func = improved_fitness_functions.F16
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 17:
        func = improved_fitness_functions.F17
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 18:
        func = improved_fitness_functions.F18
        num_genes = 2
        genotype_range = [-2, 2]
    elif function == 19:
        func = improved_fitness_functions.F19
        num_genes = 3
        genotype_range = [1, 3]
    elif function == 20:
        func = improved_fitness_functions.F20
        num_genes = 6
        genotype_range = [0, 1]
    elif function == 21:
        func = improved_fitness_functions.F21
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 22:
        func = improved_fitness_functions.F22
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 23:
        func = improved_fitness_functions.F23
        num_genes = 4
        genotype_range = [0, 10]
    return func, num_genes, genotype_range


'''This combination function is to generate all the combinations for different parameters.
There are 3072 combinations in total.'''


def combination():
    com = []
    iterations = [1000000]
    mutation_rate = [0.1, 0.18, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
    num_individuals = [100, 200]
    range_mutation = [0.01, 0.25, 0.55, 0.9, 2.0, 5.0]
    crossover_probability = [0.5, 0.6, 0.7]
    for a in iterations:
        for b in mutation_rate:
            for c in num_individuals:
                for d in range_mutation:
                    for e in crossover_probability:
                        G = [a, b, c, d, e]
                        com.append(G)
    sequence_list = [str(iterations), str(mutation_rate), str(num_individuals), str(range_mutation),
                     str(crossover_probability)]
    name = ["iterations", "mutation_rate", "num_individuals", "range_mutation", "crossover_probability"]
    with open("combinations_result_baseline.txt", 'w+', encoding='utf-8') as f:
        for x, sequence in zip(name, sequence_list):
            f.writelines("Sequence for {0} : {1}".format(x, sequence))
            f.write("\n")
        for i in range(len(com)):
            for j in range(len((com[i]))):
                f.write(str(com[i][j]))
                f.write(",")
            f.write("\n")
    return com


'''This test function is to run a combination for one function.
The inputs are a specific function, a mode, a parameter_list(combination)

first, generate a group of individuals
second, calculate the fitness values for each individual based on the chosen fitness function
third, store the minimum(the best) in a list
fourth, generate a new individual
fifth, delete the worst one
sixth, let the new one join the group (append the new one in the group)
seventh,calculate the fitness value for the new individual and compare it to others
........continue.....
return the minimum of all the iterations'''

global_opt = opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 10, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32,
                    -10.1532, -10.4028, -10.5363]


def test(function, parameter_list, opt):
    iterations = int(parameter_list[0])
    mutation_rate = parameter_list[1]
    num_individuals = int(parameter_list[2])
    range_mutation = parameter_list[3]
    crossover_probability = parameter_list[4]
    func, num_genes, genotype_range = choose_func(function)
    individuals = initialization(num_genes=num_genes, num_individual=num_individuals, genotype_range=genotype_range)
    best_generation = []
    best, worst, fit_all = fitness(individuals=individuals, func=func)
    best_generation.append(fit_all[best])
    new_individual = offspring(individuals=individuals, best_fit=best, worst_fit=worst,
                               num_genes=num_genes, mutation_rate=mutation_rate, range_mutation=range_mutation,
                               crossover_probability=crossover_probability, mutation_type=1, crossover_type=2)
    new = Individual(genotype=new_individual, num_genes=num_genes, genotype_range=genotype_range, pattern=1)

    del individuals[worst]
    del fit_all[worst]
    zipped = zip(individuals, fit_all)
    sort_zipped = sorted(zipped, key=lambda x: x[1])
    new_fit = fitness_single(individual=new, func=func)
    new_zip = (new, new_fit)
    for i in range(len(sort_zipped)):
        individual, fv = sort_zipped[i]
        if new_fit < fv:
            sort_zipped.insert(i, new_zip)
            break
        if i == len(sort_zipped) - 1:
            sort_zipped.append(new_zip)
            break
    individuals = [i for i, j in sort_zipped]
    fit_all = [j for i, j in sort_zipped]

    count = 1

    for generation in range(iterations - 1):
        count += 1
        best_individual, best_fv = sort_zipped[0]
        best_generation.append(best_fv)
        if best_fv <= opt:
            break
        new_individual = offspring(individuals=individuals, best_fit=0, worst_fit=-1,
                                   num_genes=num_genes, mutation_rate=mutation_rate,
                                   range_mutation=range_mutation, crossover_probability=crossover_probability,
                                   mutation_type=1, crossover_type=2)
        new = Individual(genotype=new_individual, num_genes=num_genes, genotype_range=genotype_range, pattern=1)
        new_fit = fitness_single(individual=new, func=func)
        new_zip = (new, new_fit)
        del sort_zipped[-1]
        del individuals[-1]
        del fit_all[-1]
        for i in range(len(sort_zipped)):
            individual, fv = sort_zipped[i]
            if new_fit < fv:
                sort_zipped.insert(i, new_zip)
                individuals.insert(i, new)
                fit_all.insert(i, new_fit)
                break
            elif i == len(sort_zipped) - 1:
                sort_zipped.append(new_zip)
                individuals.append(new)
                fit_all.append(new_fit)
                break
    return min(best_generation)


'''This multiple function is to calculate multiples runs for all the fitness functions and combinations.
For F12, I use F13 to replace F12 for now.
For the U function, I set the values to zero if it falls into the unknown interval.
For each function and combination, 10 runs.
The max,min,mean,std are also generated based on the results of 10 runs.
It is a 3D list, I saved the all the values.
'''


def multiple(Times, L, Com):
    result_list_all = []
    combination = Com
    k = ["F" + str(i) for i in range(1, 24, 1)]
    for i in range(L[0], L[1], 1):
        result_list_coloum = []
        for f in range(1, 24, 1):
            result_list = []
            for times in range(Times):
                result = test(function=f, parameter_list=combination[i], opt=global_opt[f - 1])
                result_list.append(float(result))
            result_list_coloum.append(result_list)
        if (i - L[0]) % 30 == 29:
            print("\033[0;37;45m Starting from {0}, {1} combinations are tested.\033[0m".format(L[0], i - L[0] + 1))
            print("\n")
        result_list_all.append(result_list_coloum)
    temp = np.array(result_list_all)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], 23 * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product(
                            [k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)]
                        )
    short_data = data.applymap(lambda x: '{:1.2e}'.format(x))
    return data, short_data, temp


def multipleF(Times, L, Com, function_list):
    result_list_all = []
    combination = Com
    k = ["F" + str(i) for i in function_list]
    for i in range(L[0], L[1], 1):
        result_list_coloum = []
        for f in function_list:
            result_list = []
            for times in range(Times):
                result = test(function=f, parameter_list=combination[i], opt=global_opt[f - 1])
                result_list.append(float(result))
            result_list_coloum.append(result_list)
        if (i - L[0]) % 30 == 29:
            print("\033[0;37;45m Starting from {0}, {1} combinations are tested.\033[0m".format(L[0], i - L[0] + 1))
            print("\n")
        result_list_all.append(result_list_coloum)
    temp = np.array(result_list_all)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], len(function_list) * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product(
                            [k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)]
                        )
    short_data = data.applymap(lambda x: '{:1.2e}'.format(x))
    return data, short_data, temp


'''The main function is to generate the whole data.'''

if __name__ == '__main__':
    com = combination()
    df = pd.DataFrame(data=com, index=["Combination" + str(i + 1) for i in range(len(com))],
                      columns=["iterations", "mutation_rate", "num_individuals", "range_mutation",
                               "crossover_probability"])
    df.to_csv('combinations_result_baseline.csv',
              header=True,
              index=False)

    # data, short_data, temp = multipleF(Times=10, L=[0, len(com[:5])], Com=com[:5], function_list=[1, 18, 22])
    # print(data)
    # print("\n")
    # print(short_data)
    # print("\n")
    # print(temp)

    data, short_data, temp = multipleF(Times=10, L=[0, len(com[:100])], Com=com[:100], function_list=[1, 18, 22])
    with open("Baseline_3Dlist_short_100.txt", "w") as w:
        w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
    with open("Baseline_3Dlist_long_100.txt", "w") as w:
        w.write(np.array2string(temp))
    short_data.to_csv('./Baseline_table_short_100.csv',
                      sep=',',
                      header=True,
                      index=True)

    data.to_csv('./Baseline_table_long_100.csv',
                sep=',',
                header=True,
                index=True)

    data, short_data, temp = multipleF(Times=10, L=[0, len(com[100:200])], Com=com[100:200], function_list=[1, 18, 22])
    with open("Baseline_3Dlist_short_100_200.txt", "w") as w:
        w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
    with open("Baseline_3Dlist_long_100_200.txt", "w") as w:
        w.write(np.array2string(temp))
    short_data.to_csv('./Baseline_table_short_100_200.csv',
                      sep=',',
                      header=True,
                      index=True)

    data.to_csv('./Baseline_table_long_100_200.csv',
                sep=',',
                header=True,
                index=True)

    data, short_data, temp = multipleF(Times=10, L=[0, len(com[200:])], Com=com[200:], function_list=[1, 18, 22])
    with open("Baseline_3Dlist_short_200_end.txt", "w") as w:
        w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
    with open("Baseline_3Dlist_long_200_end.txt", "w") as w:
        w.write(np.array2string(temp))
    short_data.to_csv('./Baseline_table_short_200_end.csv',
                      sep=',',
                      header=True,
                      index=True)

    data.to_csv('./Baseline_table_long_200_end.csv',
                sep=',',
                header=True,
                index=True)
