# Name: Mei Jiaojiao
# Specilization: Artificial Intelligence
# Time and date: 7/25/22 14:17
import datetime
import itertools
import random
import statistics
import sys

import numpy as np
import pandas as pd

import Fitness_Functions

pd.options.display.max_columns = None
pd.options.display.max_rows = None

np.set_printoptions(threshold=sys.maxsize)

'''The class Individual is to generate genotype and generate phenotype based on genotype.
To generate a genotype,the inputs are 1.num of genes, genotype_range which determines the range for each gene.
The genotype are generated randomly.
The local search happens from genotype to phenotypes.
Given a local search rate, for each gene, there is a probability(local search rate) to change.
Generate a random probability(0,1) and compares it with local search rate,
if random < local search, then this gene is going to change,
the way of changing is to plus a random value between(-m_range,m_range),
then the phenotype is obtained.'''


class Individual:
    def __init__(self, num_genes, genotype, genotype_range, local_search, m_range):
        if genotype:
            self.genotype = genotype
        else:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.genotype = [np.round(i, 8) for i in self.genotype]
        local_search_rate = local_search / num_genes
        k = self.genotype
        for i in range(len(k)):
            if np.random.rand() < local_search_rate:
                k[i] = k[i] + np.random.uniform(-m_range, m_range)
                k[i] = np.round(k[i], 8)
        self.phenotype = k


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


def offspring(individuals, num_genes, best_fit, worst_fit, mutation_rate, mode, range_mutation):
    n = []
    if mode == "Lamarck":
        for individual in individuals:
            n.append(individual.phenotype)
    elif mode == "Baldwin":
        for individual in individuals:
            n.append(individual.genotype)
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
    mutation_rate = mutation_rate / num_genes
    for i in range(len(result)):
        if np.random.rand() < mutation_rate:
            result[i] = result[i] + np.random.uniform(-range_mutation, range_mutation)
            result[i] = np.round(result[i], 8)
    return result


'''This initialization function is to generate the initial group
for each individual in the group, generate the genotype and the phenotype'''


def initialization(num_genes, num_individual, genotype_range, local_search, m_range):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(
            Individual(num_genes=num_genes, genotype=None, genotype_range=genotype_range, local_search=local_search,
                       m_range=m_range))
    return individuals


'''This choose_func function is to choose a specific function,
each function has its own dimensions(num_genes) and genotype_range'''


def choose_func(function):
    func = None
    num_genes = None
    genotype_range = None
    if function == 1:
        func = Fitness_Functions.f1
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 2:
        func = Fitness_Functions.f2
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 3:
        func = Fitness_Functions.f3
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 4:
        func = Fitness_Functions.f4
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 5:
        func = Fitness_Functions.f5
        num_genes = 50
        genotype_range = [-30, 30]
    elif function == 6:
        func = Fitness_Functions.f6
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 7:
        func = Fitness_Functions.f7
        num_genes = 50
        genotype_range = [-1.28, 1.28]
    elif function == 8:
        func = Fitness_Functions.f8
        num_genes = 50
        genotype_range = [-500, 500]
    elif function == 9:
        func = Fitness_Functions.f9
        num_genes = 50
        genotype_range = [-5.12, 5.12]
    elif function == 10:
        func = Fitness_Functions.f10
        num_genes = 50
        genotype_range = [-32, 32]
    elif function == 11:
        func = Fitness_Functions.f11
        num_genes = 50
        genotype_range = [-600, 600]
    elif function == 12:
        func = Fitness_Functions.f13
        num_genes = 50
        genotype_range = [-50, 50]
    elif function == 13:
        func = Fitness_Functions.f13
        num_genes = 50
        genotype_range = [-50, 50]
    elif function == 14:
        func = Fitness_Functions.f14
        num_genes = 2
        genotype_range = [-65, 65]
    elif function == 15:
        func = Fitness_Functions.f15
        num_genes = 4
        genotype_range = [-5, 5]
    elif function == 16:
        func = Fitness_Functions.f16
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 17:
        func = Fitness_Functions.f17
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 18:
        func = Fitness_Functions.f18
        num_genes = 2
        genotype_range = [-2, 2]
    elif function == 19:
        func = Fitness_Functions.f19
        num_genes = 3
        genotype_range = [1, 3]
    elif function == 20:
        func = Fitness_Functions.f20
        num_genes = 6
        genotype_range = [0, 1]
    elif function == 21:
        func = Fitness_Functions.f21
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 22:
        func = Fitness_Functions.f22
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 23:
        func = Fitness_Functions.f23
        num_genes = 4
        genotype_range = [0, 10]
    return func, num_genes, genotype_range


'''This combination function is to generate all the combinations for different parameters.
There are 3072 combinations in total.'''


def combination():
    com = []
    iterations = [500, 1000, 2000, 3000]
    mutation_rate = [0.1, 0.5, 1.0, 2.0]
    local_search = [0.1, 0.5, 1.0, 2.0]
    num_individuals = [50, 100, 150]
    m_range = [0.5, 1.0, 2.0, 5.0]
    range_mutation = [0.5, 1.0, 2.0, 5.0]
    for a in iterations:
        for b in mutation_rate:
            for c in local_search:
                for d in num_individuals:
                    for e in m_range:
                        for f in range_mutation:
                            G = [a, b, c, d, e, f]
                            com.append(G)
    sequence_list = [str(iterations), str(mutation_rate), str(local_search), str(num_individuals), str(m_range),
                     str(range_mutation)]
    name = ["iterations", "mutation_rate", "local_search", "num_individuals", "m_range", "range_mutation"]
    with open(
            "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/parameter_combinations/combinations_result.txt",
            'w+', encoding='utf-8') as f:
        for x, sequence in zip(name, sequence_list):
            f.writelines("Sequence for {0} : {1}".format(x, sequence))
            f.write("\n")
        for i in range(len(com)):
            for j in range(len((com[i]))):
                f.write(str(com[i][j]))
                f.write(",")
            f.write("\n")
    df = pd.DataFrame(data=com, index=["Combination" + str(i + 1) for i in range(len(com))],
                      columns=["iterations", "mutation_rate", "local_search", "num_individuals", "m_range",
                               "range_mutation"])
    df.to_csv(
        '/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/parameter_combinations/combinations_result.csv',
        header=True,
        index=False)
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


def test(function, mode, parameter_list,opt):
    iterations = parameter_list[0]
    mutation_rate = parameter_list[1]
    local_search = parameter_list[2]
    num_individuals = parameter_list[3]
    m_range = parameter_list[4]
    range_mutation = parameter_list[5]
    func, num_genes, genotype_range = choose_func(function)
    individuals = initialization(num_genes=num_genes, num_individual=num_individuals, genotype_range=genotype_range,
                                 local_search=local_search, m_range=m_range)
    best_generation = []
    best, worst, fit_all = fitness(individuals=individuals, func=func)
    best_generation.append(fit_all[best])
    new_individual = offspring(individuals=individuals, best_fit=best, worst_fit=worst,
                               num_genes=num_genes, mutation_rate=mutation_rate, mode=mode,
                               range_mutation=range_mutation)
    new = Individual(genotype=new_individual, num_genes=num_genes, genotype_range=genotype_range,
                     local_search=local_search,
                     m_range=m_range)
    del individuals[worst]
    individuals.append(new)
    del fit_all[worst]
    fit_all.append(fitness_single(individual=new, func=func))
    count = 1

    for generation in range(iterations - 1):
        count += 1
        best = np.argmin(fit_all)
        worst = np.argmax(fit_all)
        best_generation.append(fit_all[best])
        if fit_all[best] <= opt:
            break
        new_individual = offspring(individuals=individuals, best_fit=best, worst_fit=worst,
                                   num_genes=num_genes, mutation_rate=mutation_rate, mode=mode,
                                   range_mutation=range_mutation)
        new = Individual(genotype=new_individual, num_genes=num_genes, genotype_range=genotype_range,
                         local_search=local_search,
                         m_range=m_range)
        del individuals[worst]
        del fit_all[worst]
        individuals.append(new)
        fit_all.append(fitness_single(individual=new, func=func))

    return min(best_generation)


'''This multiple function is to calculate multiples runs for all the fitness functions and combinations.
For F12, I use F13 to replace F12 for now.
For the U function, I set the values to zero if it falls into the unknown interval.
For each function and combination, 10 runs.
The max,min,mean,std are also generated based on the results of 10 runs.
It is a 3D list, I saved the all the values.
'''


def multiple(mode, Times, L):
    result_list_all = []
    result_list_all_four = []
    com = combination()
    k = ["F" + str(i) for i in range(1, 24, 1)]
    for i in range(L[0], L[1], 1):
        result_list_coloum = []
        result_list_coloum_four = []
        for f in range(1, 24, 1):
            result_list = []
            for times in range(Times):
                result = test(function=f, mode=mode, parameter_list=com[i])
                result_list.append(float(result))
            four = [statistics.mean(result_list), statistics.stdev(result_list), np.max(result_list),
                    np.min(result_list)]
            result_list_coloum.append(result_list)
            result_list_coloum_four.append(four)
        if (i - L[0]) % 50 == 49:
            print("\033[0;37;45m Starting from {0}, {1} combinations are tested.\033[0m".format(L[0], i - L[0] + 1))
            print("\n")
        result_list_all.append(result_list_coloum)
        result_list_all_four.append(result_list_coloum_four)
    temp = np.array(result_list_all)
    temp_four = np.array(result_list_all_four)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], 23 * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product(
                            [k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=[str(mode) + str(i + 1) for i in range(L[0], L[1], 1)]
                        )
    data_four = pd.DataFrame(data=np.resize(temp_four, (L[1] - L[0], 23 * 4)).swapaxes(0, 1),
                             index=pd.MultiIndex.from_product(
                                 [k, ['Mean', 'Std', 'Max', 'Min']]),
                             columns=[str(mode) + str(i + 1) for i in range(L[0], L[1], 1)]
                             )
    short_data = data.applymap(lambda x: '{:1.2e}'.format(x))
    short_data_four = data_four.applymap(lambda x: '{:1.2e}'.format(x))
    return data, data_four, short_data, short_data_four, temp, temp_four


'''The main function is to generate the whole data.'''

 if __name__ == '__main__':
     data, data_four, short_data, short_data_four, temp, temp_four = multiple(mode="Baldwin", Times=10, L=[0, 3072])

     with open("Baldwin_3Dlist_short_1_3072.txt", "w") as w:
         w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
     with open("Baldwin_3Dlist_short_four_1_3072.txt", "w") as w:
         w.write(np.array2string(temp_four, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))

     with open("Baldwin_3Dlist_long_1_3072.txt", "w") as w:
         w.write(np.array2string(temp))
     with open("Baldwin_3Dlist_long_four_1_3072.txt", "w") as w:
         w.write(np.array2string(temp_four))

     short_data.to_csv('./Baldwin_table_short_1_3072.csv',
                       sep=',',
                       header=True,
                       index=True)
     short_data_four.to_csv('./Baldwin_table_short_four_1_3072.csv',
                            sep=',',
                            header=True,
                            index=True)

     data.to_csv('./Baldwin_table_long_1_3072.csv',
                 sep=',',
                 header=True,
                 index=True)
     data_four.to_csv('./Baldwin_table_long_four_1_3072.csv',
                      sep=',',
                      header=True,
                      index=True)

     data, data_four, short_data, short_data_four, temp, temp_four = multiple(mode="Lamarck", Times=10, L=[0, 3072])

     with open("Lamarck_3Dlist_short_1_3072.txt", "w") as w:
         w.write(np.array2string(temp, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))
     with open("Lamarck_3Dlist_short_four_1_3072.txt", "w") as w:
         w.write(np.array2string(temp_four, formatter={'float_kind': lambda x: '{:1.2e}'.format(x)}))

     with open("Lamarck_3Dlist_long_1_3072.txt", "w") as w:
         w.write(np.array2string(temp))
     with open("Lamarck_3Dlist_long_four_1_3072.txt", "w") as w:
         w.write(np.array2string(temp_four))

     short_data.to_csv('./Lamarck_table_short_1_3072.csv',
                       sep=',',
                       header=True,
                       index=True)
     short_data_four.to_csv('./Lamarck_table_short_four_1_3072.csv',
                            sep=',',
                            header=True,
                            index=True)

     data.to_csv('./Lamarck_table_long_1_3072.csv',
                 sep=',',
                 header=True,
                 index=True)
     data_four.to_csv('./Lamarck_table_long_four_1_3072.csv',
                      sep=',',
                      header=True,
                      index=True)


# this is for test the time
#if __name__ == '__main__':
#    import numpy as np
#    time1 = datetime.datetime.now()
#    print(time1)
#    test(function=1, mode="Lamarck", parameter_list=[3000, 0.1, 0.1, 50, 0.5, 5.0, 0.6],opt=0)
#    time1 = datetime.datetime.now()
#    print(time1)
