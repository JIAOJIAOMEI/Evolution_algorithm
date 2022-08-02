# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:23
import itertools
import random
import numpy as np


def offspring(individuals, num_genes, best_fit, worst_fit, mutation_rate, mode, range_mutation, crossover_probability,
              mutation_type, crossover_type):
    n = []
    if mode == "Lamarck":
        for individual in individuals:
            n.append(individual.phenotype)
    elif mode == "Baldwin":
        for individual in individuals:
            n.append(individual.genotype)

    result = []
    if crossover_type == 0:  # Probabilistic crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        partner_index = np.random.randint(0, len(n))
        parent2 = n[partner_index]
        for j in range(len(parent1)):
            if np.random.rand() < crossover_probability:
                result.append(parent1[j])
            else:
                result.append(parent2[j])
    elif crossover_type == 1:  # singe-point-crossover
        if np.random.rand() < crossover_probability:
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
        else:
            result1 = n[best_fit]
            del n[worst_fit]
            result2_index = np.random.randint(0, len(n))
            result2 = n[result2_index]
            result = random.choice([result1, result2])
    elif crossover_type == 2:  # Linear combination crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        partner_index = np.random.randint(0, len(n))
        parent2 = n[partner_index]
        for j in range(len(parent1)):
            new_j = parent1[j] * crossover_probability + parent2[j] * (1 - crossover_probability)
            result.append(new_j)
    # numpy.random.rand from uniform (in range [0,1))
    # numpy.random.normal generates samples from the normal distribution
    mutation_rate = mutation_rate / num_genes
    if mutation_type == 0:
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + np.random.uniform(-range_mutation, range_mutation)
    elif mutation_type == 1:
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + np.random.normal(loc=0, scale=2 * range_mutation, size=1) - range_mutation
    return result
