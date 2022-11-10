# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/23/22 16:08

import numpy as np


class Individual:
    def __init__(self, func, num_genes, genotype_range, genotype, pattern, local_search_rate, local_search_type, R):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.genotype = self.genotype.tolist()
        elif pattern == 1:
            self.genotype = genotype

        STD = (genotype_range[1] - genotype_range[0]) * R

        temp = self.genotype.copy()
        if local_search_type == "Uniform":  # uniform
            for i in range(len(temp)):
                if np.random.rand() < local_search_rate:
                    temp[i] = temp[i] + float(np.random.uniform(-3 * STD, 3 * STD))
                    temp[i] = max(temp[i], genotype_range[0])  # check domain
                    temp[i] = min(temp[i], genotype_range[1])
        elif local_search_type == "Normal":  # normal
            for i in range(len(temp)):
                if np.random.rand() < local_search_rate:
                    temp[i] = temp[i] + float(np.random.normal(loc=0, scale=STD, size=1))
                    temp[i] = max(temp[i], genotype_range[0])  # check domain
                    temp[i] = min(temp[i], genotype_range[1])

        if func(temp) <= func(self.genotype):
            self.phenotype = temp
        else:
            self.phenotype = self.genotype.copy()


def initialization(func, num_genes, num_individual, genotype_range, local_search_rate, local_search_type, R):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(Individual(func=func, num_genes=num_genes, genotype=None,
                                      genotype_range=genotype_range, pattern=0, local_search_rate=local_search_rate,
                                      local_search_type=local_search_type, R=R))
    return individuals
