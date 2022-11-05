# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:48

import numpy as np
import pandas as pd
from colorama import Fore

from cal_fitness import fitness_single, fitness
from functions_parameter import choose_func
from InitializationSSGA import initialization, Individual
from offspring import offspring

global_opt = opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 50, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32,
                    -10.1532, -10.4028, -10.5363]


def test(function, parameter_list, opt):
    # [['iterations', 'mutation_rate', 'num_individuals', 'crossover_probability', 'Mutation_type', 'Crossover_type', 'R']]
    # iterations = parameter_list[0]
    iterations = 1000000
    mutation_rate = parameter_list[1]
    num_individuals = int(parameter_list[2])
    crossover_probability = parameter_list[3]
    mutation_type = parameter_list[4]
    crossover_type = parameter_list[5]
    R = parameter_list[6]

    func, num_genes, genotype_range = choose_func(function)
    individuals = initialization(num_genes=num_genes, num_individual=num_individuals, genotype_range=genotype_range)
    best_generation = []
    best, worst, fit_all = fitness(individuals=individuals, func=func)
    best_generation.append(fit_all[best])
    new_individual = offspring(individuals=individuals, best_fit=best, worst_fit=worst, num_genes=num_genes,
                               mutation_rate=mutation_rate, crossover_probability=crossover_probability,
                               mutation_type=mutation_type,
                               crossover_type=crossover_type, genotype_range=genotype_range, R=R)
    new = Individual(num_genes=num_genes, genotype=new_individual, genotype_range=genotype_range, pattern=1)

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
    budget = num_individuals
    similarity_population = sum(
        [euclidean_distance(other.phenotype, individuals[0].phenotype) for other in individuals[1:]])
    stuck = 0

    for generation in range(iterations - 1):
        count += 1
        best_individual, best_fv = sort_zipped[0]

        best_generation.append(best_fv)
        # if generation % 10000 == 9998:
        #     print(Fore.BLUE + f'{best_fv:.5E} is best, minima is {opt},generation is {generation},similarity is {similarity_population}')
        # print(best_individual.genotype)
        # current_optimal = precision_f(best_fv=best_fv, f=function)
        # if current_optimal <= opt:
        #     print(f"current optimal is {current_optimal},global minima is {opt},similarity is {similarity_population}")
        #     break

        new_individual = offspring(individuals=individuals, best_fit=0, worst_fit=-1, num_genes=num_genes,
                                   mutation_rate=mutation_rate,
                                   crossover_probability=crossover_probability, mutation_type=mutation_type,
                                   crossover_type=crossover_type, genotype_range=genotype_range, R=R)
        new = Individual(num_genes=num_genes, genotype=new_individual, genotype_range=genotype_range, pattern=1)

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
        similarity_population = sum(
            [euclidean_distance(other.phenotype, individuals[0].phenotype) for other in individuals[1:]])
        budget = budget + 1
        if similarity_population < 0.0001:
            stuck = stuck + 1
        else:
            stuck = 0
        if stuck >= 5000:
            break

    return min(best_generation), budget, similarity_population


def multipleF(Times, L, Com, function_list):
    result_list_all = []
    budget_list_all = []
    similarity_list_all = []
    combination = Com
    k = ["F" + str(i) for i in function_list]
    for i in range(L[0], L[1], 1):
        result_list_coloum = []
        budget_list_coloum = []
        similarity_list_coloum = []
        for f in function_list:
            print(Fore.RED + f"Now testing Function{f}")
            result_list = []
            budget_list = []
            similarity_list = []
            for times in range(Times):
                print(Fore.YELLOW + f"Time is {times}")
                result, budget, similarity = test(function=f, parameter_list=combination, opt=global_opt[f - 1])
                result_list.append(float(result))
                budget_list.append(float(budget))
                similarity_list.append(similarity)
            result_list_coloum.append(result_list)
            budget_list_coloum.append(budget_list)
            similarity_list_coloum.append(similarity_list)
        result_list_all.append(result_list_coloum)
        budget_list_all.append(budget_list_coloum)
        similarity_list_all.append(similarity_list_coloum)
    temp = np.array(result_list_all)
    data = pd.DataFrame(data=np.resize(temp, (L[1] - L[0], len(function_list) * Times)).swapaxes(0, 1),
                        index=pd.MultiIndex.from_product([k, ["Times" + str(times + 1) for times in range(Times)]]),
                        columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)])
    temp_budget = np.array(budget_list_all)
    data_budget = pd.DataFrame(data=np.resize(temp_budget, (L[1] - L[0], len(function_list) * Times)).swapaxes(0, 1),
                               index=pd.MultiIndex.from_product(
                                   [k, ["Times" + str(times + 1) for times in range(Times)]]),
                               columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)])
    temp_similarity = np.array(similarity_list_all)
    data_similarity = pd.DataFrame(
        data=np.resize(temp_similarity, (L[1] - L[0], len(function_list) * Times)).swapaxes(0, 1),
        index=pd.MultiIndex.from_product(
            [k, ["Times" + str(times + 1) for times in range(Times)]]),
        columns=["Combination" + str(i + 1) for i in range(L[0], L[1], 1)])
    return data, data_budget, data_similarity


def precision_f(best_fv, f):
    f = "F" + str(f)
    if f in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F10", "F11", "F12", "F13", "F14", "F18"]:
        return np.round(best_fv, 0)
    elif f in ["F17"]:
        return np.round(best_fv, 3)
    elif f in ["F8", "F19", "F20"]:
        return np.round(best_fv, 2)
    elif f in ["F15", "F16", "F21", "F22", "F23"]:
        return np.round(best_fv, 4)


def euclidean_distance(x, y):
    return np.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
