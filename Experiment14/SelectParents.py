# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/2/23 01:49
import random
from typing import List, Any


# Selection methond: Best and worst
# Return the parents

def best_and_worst(individuals):
    # return a list of the best and worst individuals
    # the first one is the best individual
    # the second one is the worst individual
    eligible_individuals = [individuals[0]]
    eligible_partners = [individuals[:-1]]
    non_eligible_individuals = [individuals[-1]]
    return eligible_individuals, eligible_partners, non_eligible_individuals


# Selection methond: sorted
# Based on the population, which is created by create_individuals in CreatePopulation.py
# Select the parents based on ranking self.rank of the individuals
# Return the parents

def sorted_selection(individuals, gg):
    size = int(gg * len(individuals))
    # noneligible_individuals are the last individuals in the individuals list
    # the first individuals in the individuals list are the eligible individuals
    eligible_individuals = [individuals[0:size]]
    eligible_partners = [individuals[:len(individuals) - size]]
    non_eligible_individuals = [individuals[len(individuals) - size:]]
    return eligible_individuals, eligible_partners, non_eligible_individuals


# Selection methond: rulette wheel
# use individual.fitness to calculate the probability of being selected
# the probability of being selected is the fitness of the individual divided by the sum of all the fitnesses
# use rulette wheel to select the N non_eligible_parents, N = int(population_size*gg)
# take the inverse of 1-probability
# use rulette wheel to select the N eligible_parents
# eligible_partners are the individuals in the population except the non_eligible_individuals

def rulette_wheel(individuals, gg):
    # calculate the sum of all the fitnesses
    sum_fitness = 0
    for individual in individuals:
        sum_fitness += individual.fitness
    # calculate the probability of being selected
    probability = []
    for individual in individuals:
        probability.append(individual.fitness / sum_fitness)
    # use rulette wheel to select the N non_eligible_parents, N = int(population_size*gg)
    non_eligible_individuals: list[Any] = []
    for i in range(int(len(individuals) * gg)):
        # generate a random number between 0 and 1
        random_num = random.random()
        # calculate the sum of the probabilities
        sum_probability = 0
        for j in range(len(probability)):
            sum_probability += probability[j]
            if random_num < sum_probability:
                non_eligible_individuals.append(individuals[j])
                break

    # use rulette wheel to select the N eligible_parents
    eligible_individuals = []
    for i in range(int(len(individuals) * gg)):
        # generate a random number between 0 and 1
        random_num = random.random()
        # calculate the sum of the probabilities
        sum_probability = 0
        for j in range(len(probability)):
            sum_probability += (1 - probability[j])
            if random_num < sum_probability:
                eligible_individuals.append(individuals[j])
                break

    # eligible_partners are the individuals in the population except the non_eligible_individuals
    eligible_partners = []
    for individual in individuals:
        if individual not in non_eligible_individuals:
            eligible_partners.append(individual)

    return eligible_individuals, eligible_partners, non_eligible_individuals
