# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:48

import numpy as np
import pandas as pd
from Timer import Timer

from cal_fitness import fitness_single, fitness
from functions_parameter import choose_func
from initialization import initialization, Individual
from offspring import offspring

global_opt = opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32,
                    -10.1532, -10.4028, -10.5363]

# t1 = Timer()


def test(function, mode, parameter_list, opt, mutation_type, crossover_type, local_search_type):
    iterations = 1000
    mutation_rate = parameter_list[1]
    local_search = mutation_rate
    num_individuals = int(parameter_list[2])
    range_mutation = parameter_list[3]
    local_search_range = range_mutation
    crossover_probability = parameter_list[4]

    func, num_genes, genotype_range = choose_func(function)
    individuals = initialization(num_genes=num_genes, num_individual=num_individuals, genotype_range=genotype_range,
                                 local_search=local_search, local_search_range=local_search_range,
                                 local_search_type=local_search_type)
    best_generation = []
    best, worst, fit_all = fitness(individuals=individuals, func=func)
    best_generation.append(fit_all[best])
    new_individual = offspring(individuals=individuals, best_fit=best, worst_fit=worst,
                               num_genes=num_genes, mutation_rate=mutation_rate, mode=mode,
                               range_mutation=range_mutation, crossover_probability=crossover_probability,
                               mutation_type=mutation_type, crossover_type=crossover_type,
                               genotype_range=genotype_range)
    new = Individual(num_genes=num_genes, genotype=new_individual, genotype_range=genotype_range,
                     local_search=local_search, local_search_range=local_search_range, pattern=1,
                     local_search_type=local_search_type)

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
        if round(best_fv, 4) <= opt:
            break
        # t1.start()
        new_individual = offspring(individuals=individuals, best_fit=0, worst_fit=-1,
                                   num_genes=num_genes, mutation_rate=mutation_rate, mode=mode,
                                   range_mutation=range_mutation, crossover_probability=crossover_probability,
                                   mutation_type=mutation_type, crossover_type=crossover_type,
                                   genotype_range=genotype_range)
        new = Individual(num_genes=num_genes, genotype=new_individual, genotype_range=genotype_range,
                         local_search=local_search, local_search_range=local_search_range, pattern=1,
                         local_search_type=local_search_type)
        # t1.end()
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


# def Caltime():
#     print(t1.total_time)


def multiple(mode, Times, L, Com, type_list):
    result_list_all = []
    combination = Com
    k = ["F" + str(i) for i in range(1, 24, 1)]
    for i in range(L[0], L[1], 1):
        result_list_col = []
        for f in range(1, 24, 1):
            result_list = []
            for times in range(Times):
                result = test(function=f, mode=mode, parameter_list=combination, opt=global_opt[f - 1],
                              mutation_type=type_list[0],
                              crossover_type=type_list[1],
                              local_search_type=type_list[2])
                result_list.append(float(result))
            result_list_col.append(result_list)
        result_list_all.append(result_list_col)
    temp = np.array(result_list_all)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], 23 * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product(
                            [k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=[str(mode) + str(i + 1) for i in range(L[0], L[1], 1)])
    # short_data = data.applymap(lambda x: '{:1.2e}'.format(x))
    return data, temp


def multipleF(mode, Times, L, Com, type_list,function_list):
    result_list_all = []
    combination = Com
    k = ["F" + str(i) for i in function_list]
    for i in range(L[0], L[1], 1):
        result_list_coloum = []
        for f in function_list:
            result_list = []
            for times in range(Times):
                result = test(function=f, mode=mode, parameter_list=combination, opt=global_opt[f - 1],
                              mutation_type=type_list[0],
                              crossover_type=type_list[1],
                              local_search_type=type_list[2])
                result_list.append(float(result))
            result_list_coloum.append(result_list)
        # if (i - L[0]) % 30 == 29:
        #     print("\033[0;37;45m Starting from {0}, {1} combinations are tested.\033[0m".format(L[0], i - L[0] + 1))
        #     print("\n")
        result_list_all.append(result_list_coloum)
    temp = np.array(result_list_all)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], len(function_list) * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product(
                            [k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)]
                        )
    # short_data = data.applymap(lambda x: '{:1.2e}'.format(x))
    return data, temp
