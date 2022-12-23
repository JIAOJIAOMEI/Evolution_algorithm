# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:33
import numpy as np


def fitness(individuals, func):
    fit = []
    # fit1=[]
    for individual in individuals:
        # fit1.append(func(individual.phenotype))
        fit.append(individual.phenotype_fitness)
    # print(fit==fit1,"group")
    best_fit = np.argmin(fit)
    worst_fit = np.argmax(fit)
    return best_fit, worst_fit, fit


def fitness_single(individual, func):
    # print(func(individual.phenotype)==individual.phenotype_fitness,"single")
    return individual.phenotype_fitness
