# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 19:25

import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import pandas as pd

from LocalSearch import local_search


# create an Individual class, with the parameter: func, num_genes, genotype_range, mutation_rate, crossover_rate,mutation_type, crossover_type，search_radius
# func: the function to be optimized, it can be any function in TestFunctions.py
# num_genes: the number of genes in the individual, which is the dimension of the function, each gene is a float number within the range of genotype_range
# genotype_range: the range of the genes in the individual, which is the range of the function, a list with two elements, the first is the lower bound, the second is the upper bound
# mutation_rate: the probability of mutation, a float number between 0 and 1
# crossover_rate: the probability of crossover，a float number between 0 and 1
# mutation_type: the type of mutation, it can be 'uniform', 'gaussian', 'frequency_based'，it is a method in Mutation.py
# crossover_type: the type of crossover, it can be 'one-point', 'two-point', 'uniform', 'arithmetic', 'heuristic',"Roulette wheel", it is a method in Crossover.py
# genotype is a list of genes, which is a list of float numbers, the length of genotype is num_genes, the range of each gene is genotype_range, the initial value of genotype is a list of random float numbers within the range of genotype_range, the length of the list is num_genes
# phenotype is also a list, which is as same length as genotype, the range of each gene is genotype_range, the initial value of phenotype is the same as genotype
# fitness is the fitness of the individual, it is a float number, it is calculated by the function func, the initial value of fitness is the fitness of the phenotype
# if genotype is not given then create a random genotype
# if genotype is given then use the given genotype to create the individual
# search_radius is a float number, it is used to calculate the range of mutation, the range of mutation is search_radius*genotype_range

class Individual:
    def __init__(self, func, num_genes, genotype_range, mutation_rate, crossover_rate, mutation_type, crossover_type,search_radius,local_search_type=None,local_search_rate=None,
                 genotype=None):
        self.rank = None
        self.func = func
        self.num_genes = num_genes
        self.genotype_range = genotype_range
        self.search_radius = search_radius
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.mutation_type = mutation_type
        self.crossover_type = crossover_type
        if genotype is None:
            self.genotype = [random.uniform(genotype_range[0], genotype_range[1]) for _ in range(num_genes)]
        else:
            self.genotype = genotype
        # if locao_search_method is None, phenotype is the same as genotype
        # if local_search_type is not None, phenotype is the result of local search
        if local_search_type == "None":
            self.phenotype = self.genotype.copy()
        else:
            self.phenotype = local_search(genotype, genotype_range, num_genes, local_search_type, local_search_rate)
        # calculate the fitness of the genotype and phenotype
        # the smaller one is the fitness
        self.fitness = min(self.func(self.genotype), self.func(self.phenotype))


# create a method to generate multiple individuals, with the parameter: population_size, func, num_genes, genotype_range, mutation_rate, crossover_rate,mutation_type, crossover_type
# population_size: the number of individuals in the population, it is an integer
# return a list of individuals, the length of the list is population_size

def create_individuals(population_size, func, num_genes, genotype_range, mutation_rate, crossover_rate, mutation_type,
                       crossover_type, search_radius, local_search_type, local_search_rate):
    individuals = []
    for _ in range(population_size):
        individuals.append(Individual(func, num_genes, genotype_range, mutation_rate, crossover_rate, mutation_type,
                                      crossover_type,search_radius,local_search_type,local_search_rate))
    # sort the individuals by their fitness by an ascending order
    # add a new parameter to the individuals, which is the rank of the individual,
    # the rank of the individual is the index of the individual in the sorted list, if the rank is 1, then the fitness is the smallest
    individuals.sort(key=lambda x: x.fitness)
    for i in range(len(individuals)):
        individuals[i].rank = i + 1
    return individuals

