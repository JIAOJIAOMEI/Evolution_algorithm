# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/2/23 01:49
import random


# Selection methond: Best and worst
# Return the parents

def best_and_worst(individuals):
    # return a list of the best and worst individuals
    # the first one is the best individual
    # the second one is the worst individual
    eligible_individuals = [individuals[0]]
    eligible_partners = [individuals[:-1]]
    non_eligible_individuals = [individuals[-1]]
    return eligible_individuals, eligible_partners,non_eligible_individuals


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

