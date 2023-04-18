# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/2/23 01:49
import random
from typing import List, Any

import numpy as np


# Selection methond: Best and worst
# Return the parents

def SSGA(individuals):
    # return a list of the best and worst individuals
    # the first one is the best individual
    # the second one is the worst individual
    eligible_individuals = [individuals[0]]
    eligible_partners = individuals[:-1]
    non_eligible_individuals = [individuals[-1]]
    return eligible_individuals, eligible_partners, non_eligible_individuals


# Selection methond: sorted
# Based on the population, which is created by create_individuals in CreatePopulation.py
# Select the parents based on ranking self.rank of the individuals
# Return the parents

def sorted_selection_part(individuals, gg):
    size = int(gg * len(individuals))
    if size == 0:
        size = 1
    elif size >= len(individuals):
        size = len(individuals) - 1
    # noneligible_individuals are the last individuals in the individuals list
    # the first individuals in the individuals list are the eligible individuals
    eligible_individuals = individuals[0:size]
    eligible_partners = individuals[:len(individuals) - size]
    non_eligible_individuals = individuals[len(individuals) - size:]
    return eligible_individuals, eligible_partners, non_eligible_individuals


def sorted_selection_all(individuals, gg):
    size = int(gg * len(individuals))
    # make sure that at least one individual is selected
    if size == 0:
        size = 1
    elif size >= len(individuals):
        size = len(individuals) - 1
    # noneligible_individuals are the last individuals in the individuals list
    # the first individuals in the individuals list are the eligible individuals
    eligible_individuals = individuals[0:size]
    eligible_partners = individuals
    non_eligible_individuals = individuals[len(individuals) - size:]
    return eligible_individuals, eligible_partners, non_eligible_individuals


# Selection methond: rulette wheel
# use individual.fitness to calculate the probability of being selected
# the probability of being selected is the fitness of the individual divided by the sum of all the fitnesses
# use rulette wheel to select the N non_eligible_parents, N = int(population_size*gg)
# take the inverse of 1-probability
# use rulette wheel to select the N eligible_parents
# eligible_partners are the individuals in the population except the non_eligible_individuals

import colorama


def roulette_Wheel_Select(individuals, gg):
    # calculate the sum of all the fitnesses adn the probability of each individual, one line code, use abs() to make sure that the fitness is positive
    sum_fitness = sum([abs(individual.fitness) for individual in individuals])
    probability = [abs(individual.fitness) / sum_fitness for individual in individuals]
    # print in red
    # print(colorama.Fore.RED + "probability: " + str(probability))
    # sum of the probability
    # print(colorama.Fore.RED + "sum of the probability: " + str(sum(probability)))
    # calculate the inverse of 1-probability
    inverse_probability = [1 - i for i in probability]
    # normalize the inverse_probability
    inverse_probability = [i / sum(inverse_probability) for i in inverse_probability]
    # print in green
    # print(colorama.Fore.GREEN + "inverse_probability: " + str(inverse_probability))
    # sum of the inverse_probability
    # print(colorama.Fore.GREEN + "sum of the inverse_probability: " + str(sum(inverse_probability)))

    size = int(gg * len(individuals))
    if size == 0:
        size = 1
    elif size >= len(individuals):
        size = len(individuals) - 1

    # use rulette wheel to select the N non_eligible_parents, N = int(population_size*gg), one line code
    non_eligible_individuals = np.random.choice(individuals, size, p=probability, replace=False)
    # use rulette wheel to select the N eligible_parents, one line code
    eligible_individuals = np.random.choice(individuals, size, p=inverse_probability, replace=False)
    # eligible_partners are the individuals in the population except the non_eligible_individuals
    eligible_partners = [individual for individual in individuals if individual not in non_eligible_individuals]

    return eligible_individuals, eligible_partners, non_eligible_individuals


# write a function to summary the selection methods
# return the parents
def selection(individuals, gg, selection_method):
    if selection_method == "SSGA":
        eligible_individuals, eligible_partners, non_eligible_individuals = SSGA(individuals)
    elif selection_method == "sorted_selection_part":
        eligible_individuals, eligible_partners, non_eligible_individuals = sorted_selection_part(individuals, gg)
    elif selection_method == "sorted_selection_all":
        eligible_individuals, eligible_partners, non_eligible_individuals = sorted_selection_all(individuals, gg)
    elif selection_method == "roulette_Wheel_Select":
        eligible_individuals, eligible_partners, non_eligible_individuals = roulette_Wheel_Select(individuals, gg)
    else:
        print("No such selection method")
        return None
    return eligible_individuals, eligible_partners, non_eligible_individuals



