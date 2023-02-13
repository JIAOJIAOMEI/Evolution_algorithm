# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 23:40
import random

import numpy as np


# parameters: genotype, genotype_range, num_genes, local_search_type, local_search_rate
# local_search_type: 1: "uniform",2: "guass" 2: hill climbing, 3: simulated annealing
# local_search_rate: a float number between 0 and 1
# based on the local search method, create a phenotype based on the genotype
# return the phenotype

def uniform_local_search(genotype, genotype_range, num_genes, local_search_rate, search_radius):
    STD = (genotype_range[1] - genotype_range[0]) * search_radius
    temp = genotype.copy()
    for i in range(num_genes):
        if np.random.rand() < local_search_rate:
            temp[i] = temp[i] + float(np.random.uniform(-3 * STD, 3 * STD))
            temp[i] = max(temp[i], genotype_range[0])  # check domain
            temp[i] = min(temp[i], genotype_range[1])
    phenotype = temp
    return phenotype


def guass_local_search(genotype, genotype_range, num_genes, local_search_rate, search_radius):
    STD = (genotype_range[1] - genotype_range[0]) * search_radius
    temp = genotype.copy()
    for i in range(num_genes):
        if np.random.rand() < local_search_rate:
            temp[i] = temp[i] + float(np.random.normal(loc=0, scale=STD, size=1))
            temp[i] = max(temp[i], genotype_range[0])  # check domain
            temp[i] = min(temp[i], genotype_range[1])
    phenotype = temp
    return phenotype


import colorama


def neighbor_search(genotype, num_genes, local_search_rate):
    # print(colorama.Fore.GREEN + "neighbor_search" + colorama.Fore.RESET)
    phenotype = []
    # if a random number is less than local_search_rate,each gene in the phenotype is the minimum of the absolute value of gene in the genotype,the absolute value of front gene and the absolute value of back gene
    #  otherwise it is the absolute gene in the genotype
    # for the first one and the last one, only compare with the front one and the back one
    for i in range(num_genes):
        if np.random.rand() < local_search_rate:
            if i == 0:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i + 1])))
            elif i == num_genes - 1:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i - 1])))
            else:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i - 1]), abs(genotype[i + 1])))
        else:
            phenotype.append(abs(genotype[i]))

    # print(colorama.Fore.GREEN + "genotype: " + str(genotype) + colorama.Fore.RESET)
    return phenotype


def local_search(genotype, genotype_range, num_genes, local_search_type, local_search_rate, search_radius):
    phenotype = []
    if local_search_type == "Uniform":
        phenotype = uniform_local_search(genotype, genotype_range, num_genes, local_search_rate, search_radius)
    elif local_search_type == "Normal":
        phenotype = guass_local_search(genotype, genotype_range, num_genes, local_search_rate, search_radius)
    elif local_search_type == "neighbor_search":
        phenotype = neighbor_search(genotype, num_genes, local_search_rate)
    return phenotype
