# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:31
import numpy as np


class Individual:
    def __init__(self, num_genes,genotype_range,genotype,local_search, m_range,pattern):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
        elif pattern ==1:
            self.genotype = genotype
        local_search_rate = local_search / num_genes
        k = self.genotype
        for i in range(len(k)):
            if np.random.rand() < local_search_rate:
                k[i] = k[i] + np.random.uniform(-m_range, m_range)
        self.phenotype = k


def initialization(num_genes, num_individual, genotype_range, local_search, m_range):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(
            Individual(num_genes=num_genes,genotype=None,genotype_range=genotype_range, local_search=local_search,
                       m_range=m_range,pattern=0))
    return individuals
