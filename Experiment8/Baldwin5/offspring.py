# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:23
import itertools
import random

import numpy as np


def offspring(individuals, num_genes, best_fit, worst_fit, mutation_rate, mode, range_mutation, crossover_probability,
              mutation_type, crossover_type, genotype_range):
    n = []
    if mode == "Lamarck":
        n = [individual.phenotype for individual in individuals]
    elif mode == "Baldwin":
        n = [individual.genotype for individual in individuals]

    result = []
    if crossover_type == "Probabilistic_crossover":  # Probabilistic crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        parent2 = random.choice(n)
        for j in range(len(parent1)):
            if np.random.rand() < crossover_probability:
                result.append(parent1[j])
            else:
                result.append(parent2[j])
    elif crossover_type == "Singe_point_crossover":  # singe-point-crossover
        if np.random.rand() < crossover_probability:
            cross_location = np.random.randint(0, num_genes)
            parent1 = n[best_fit]
            part1 = parent1[:cross_location]
            part2 = parent1[cross_location:]
            del n[worst_fit]
            parent2 = random.choice(n)
            pindex_part1 = parent2[:cross_location]
            pindex_part2 = parent2[cross_location:]
            result1 = list(itertools.chain(pindex_part1, part2))
            result2 = list(itertools.chain(part1, pindex_part2))
            result = random.choice([result1, result2])
        else:
            result1 = n[best_fit]
            del n[worst_fit]
            result2 = random.choice(n)
            result = random.choice([result1, result2])
    elif crossover_type == "Linear_combination_crossover":  # Linear combination crossover
        parent1 = n[best_fit]
        del n[worst_fit]
        parent2 = random.choice(n)
        for j in range(len(parent1)):
            new_j = parent1[j] * crossover_probability + parent2[j] * (1 - crossover_probability)
            result.append(new_j)
    mutation_rate = mutation_rate / num_genes
    if mutation_type == "Uniform":
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + float(np.random.uniform(-range_mutation, range_mutation))
                if result[i] < genotype_range[0]:  # check domain
                    result[i] = genotype_range[0]
                elif result[i] > genotype_range[1]:
                    result[i] = genotype_range[1]
    elif mutation_type == "Normal":
        for i in range(len(result)):
            if np.random.rand() < mutation_rate:
                result[i] = result[i] + float(
                    np.random.normal(loc=0, scale=2 * range_mutation, size=1) - range_mutation)
                if result[i] < genotype_range[0]:  # check domain
                    result[i] = genotype_range[0]
                elif result[i] > genotype_range[1]:
                    result[i] = genotype_range[1]
    return result
