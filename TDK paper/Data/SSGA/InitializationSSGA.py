# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/12/22 14:46

import numpy as np


class Individual:
    def __init__(self, num_genes, genotype_range, genotype, pattern):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.genotype = self.genotype.tolist()
        elif pattern == 1:
            self.genotype = genotype

        self.phenotype = self.genotype.copy()


def initialization(num_genes, num_individual, genotype_range):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(Individual(num_genes=num_genes, genotype=None, genotype_range=genotype_range, pattern=0))
    return individuals
