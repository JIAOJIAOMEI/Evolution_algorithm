# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:31
import numpy as np


class Individual:
    def __init__(self, func, num_phenotypes, num_genes, genotype_range, genotype, local_search, local_search_range,
                 pattern, local_search_type, local_pattern_type):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.genotype = self.genotype.tolist()
        elif pattern == 1:
            self.genotype = genotype
        local_search_rate = local_search / num_genes

        if local_pattern_type == 0:
            self.phenotype = best_multi_phenotype(self.genotype, local_search_type, num_phenotypes, local_search_rate,
                                                  local_search_range, genotype_range, func)
        elif local_pattern_type == 1:
            self.phenotype = best_geno_pheno(self.genotype, local_search_type, local_search_rate, local_search_range,
                                             genotype_range, func)


def best_geno_pheno(genotype, local_search_type, local_search_rate, local_search_range, genotype_range, func):
    k = genotype.copy()
    if local_search_type == "Uniform":  # uniform
        for i in range(len(k)):
            if np.random.rand() < local_search_rate:
                k[i] = k[i] + float(np.random.uniform(-local_search_range, local_search_range))
                if k[i] < genotype_range[0]:  # check domain
                    k[i] = genotype_range[0]
                elif k[i] > genotype_range[1]:
                    k[i] = genotype_range[1]
    elif local_search_type == "Normal":  # normal
        for i in range(len(k)):
            if np.random.rand() < local_search_rate:
                k[i] = k[i] + float(np.random.normal(loc=0, scale=2 * local_search_range, size=1) - local_search_range)
                if k[i] < genotype_range[0]:  # check domain
                    k[i] = genotype_range[0]
                elif k[i] > genotype_range[1]:
                    k[i] = genotype_range[1]
    phenotype = k
    if func(genotype) <= func(phenotype):
        return genotype
    else:
        return phenotype


def best_multi_phenotype(genotype, local_search_type, num_phenotypes, local_search_rate, local_search_range,
                         genotype_range, func):
    phenotype_lst = [genotype]
    if local_search_type == "Uniform":  # uniform
        for num in range(num_phenotypes):
            k = genotype.copy()
            for i in range(len(k)):
                if np.random.rand() < local_search_rate:
                    k[i] = k[i] + float(np.random.uniform(-local_search_range, local_search_range))
                    if k[i] < genotype_range[0]:  # check domain
                        k[i] = genotype_range[0]
                    elif k[i] > genotype_range[1]:
                        k[i] = genotype_range[1]
            phenotype_lst.append(k)
    elif local_search_type == "Normal":  # normal
        for num in range(num_phenotypes):
            k = genotype.copy()
            for i in range(len(k)):
                if np.random.rand() < local_search_rate:
                    k[i] = k[i] + float(
                        np.random.normal(loc=0, scale=2 * local_search_range, size=1) - local_search_range)
                    if k[i] < genotype_range[0]:  # check domain
                        k[i] = genotype_range[0]
                    elif k[i] > genotype_range[1]:
                        k[i] = genotype_range[1]
            phenotype_lst.append(k)
    phenotype_fitness_lst = [func(i) for i in phenotype_lst]
    best_fit = np.argmin(phenotype_fitness_lst)
    phenotype = phenotype_lst[best_fit]
    return phenotype


def initialization(func, num_genes, num_phenotypes, num_individual, genotype_range, local_search, local_search_range,
                   local_search_type, local_pattern_type):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(Individual(func=func, num_phenotypes=num_phenotypes, num_genes=num_genes, genotype=None,
                                      genotype_range=genotype_range, local_search=local_search,
                                      local_search_range=local_search_range, pattern=0,
                                      local_search_type=local_search_type, local_pattern_type=local_pattern_type))
    return individuals
