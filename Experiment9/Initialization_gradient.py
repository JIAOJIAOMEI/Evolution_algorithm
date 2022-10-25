# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/23/22 16:08

import numpy as np


class Individual:
    def __init__(self, func, num_genes, genotype_range, genotype, pattern, K, L, deltah):
        if pattern == 0:
            self.genotype = np.random.uniform(genotype_range[0], genotype_range[1], size=num_genes)
            self.genotype = self.genotype.tolist()
        elif pattern == 1:
            self.genotype = genotype

        self.phenotype = gradient_search(genotype=self.genotype, func=func, num_genes=num_genes, K=K, L=L,deltah=deltah,genotype_range=genotype_range)


def gradient_search(genotype, func, num_genes, K, L, deltah, genotype_range):
    best_sample = 0
    g_variable = [i for i in genotype]
    K = np.ceil(K*num_genes)
    for i in range(L):  # l iterations
        k_dimensions = np.random.choice(num_genes, size=int(K), replace=False)  # choose k randomly without replacement
        k_list = []
        for k in k_dimensions:
            g = g_variable.copy()
            g[k] = g[k] + deltah
            g[k] = min(g[k],genotype_range[1])  # only change ki dimension
            g[k] = max(g[k],genotype_range[0]) # domian-checking
            k_list.append(g)
        fit_g_variable = func(g_variable)
        gradient_k_lst = [(func(i) - fit_g_variable)/deltah for i in k_list]  # calculate gradient for ki separately
        abs_list = [abs(i) for i in gradient_k_lst]  # take absolute value
        best_sample_index = int(np.argmax(abs_list))  # find the index of max value
        best_sample = k_list[best_sample_index]  # find best sample, length of best sample = length of genotype
        index = k_dimensions[best_sample_index]  # find where the best sample changed: ki of best sample
        if abs_list[best_sample_index] == gradient_k_lst[best_sample_index]:
            best_sample[index] = max(best_sample[index] - 2 * deltah,genotype_range[0])
            best_sample[index] = min(best_sample[index],genotype_range[1])
        g_variable = best_sample.copy()
    if func(best_sample)<= func(genotype):
        return best_sample
    else:
        return genotype


def initialization(func, num_genes, num_individual, genotype_range, K, L, deltah):
    individuals = []
    for _ in range(0, num_individual):
        individuals.append(Individual(func=func, num_genes=num_genes, genotype=None,
                                      genotype_range=genotype_range, pattern=0, deltah=deltah, K=K, L=L))
    return individuals
