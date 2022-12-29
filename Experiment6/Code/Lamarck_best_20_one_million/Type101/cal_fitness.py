# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:33
import numpy as np


def fitness(individuals, func):
    fit = []
    for individual in individuals:
        # print(individual.phenotype)
        fit.append(func(individual.phenotype))
    # print(fit)
    best_fit = np.argmin(fit)
    worst_fit = np.argmax(fit)
    return best_fit, worst_fit, fit


def fitness_single(individual, func):
    return func(individual.phenotype)