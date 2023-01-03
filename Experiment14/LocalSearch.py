# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 23:40
import random


# parameters: genotype, genotype_range, num_genes, local_search_type, local_search_rate
# local_search_type: 1: "uniform",2: "guass" 2: hill climbing, 3: simulated annealing
# local_search_rate: a float number between 0 and 1
# based on the local search method, create a phenotype based on the genotype
# return the phenotype

def uniform_local_search(genotype, genotype_range, num_genes, local_search_rate):
    phenotype = []
    for i in range(num_genes):
        if random.random() < local_search_rate:
            phenotype.append(random.uniform(genotype_range[0], genotype_range[1]))
        else:
            phenotype.append(genotype[i])
    return phenotype


def guass_local_search(genotype, genotype_range, num_genes, local_search_rate):
    phenotype = []
    for i in range(num_genes):
        if random.random() < local_search_rate:
            phenotype.append(random.gauss(genotype[i], (genotype_range[1] - genotype_range[0]) / 6))
        else:
            phenotype.append(genotype[i])
    return phenotype


def hill_climbing_local_search(genotype, num_genes, local_search_rate):
    phenotype = []
    # if a random number is less than local_search_rate,each gene in the phenotype is the minimum of the absolute value of gene in the genotype,the absolute value of front gene and the absolute value of back gene
    #  otherwise it is the absolute gene in the genotype
    # for the first one and the last one, only compare with the front one and the back one
    for i in range(num_genes):
        if random.random() < local_search_rate:
            if i == 0:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i + 1])))
            elif i == num_genes - 1:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i - 1])))
            else:
                phenotype.append(min(abs(genotype[i]), abs(genotype[i - 1]), abs(genotype[i + 1])))
        else:
            phenotype.append(abs(genotype[i]))
    return phenotype


def local_search(genotype, genotype_range, num_genes, local_search_type, local_search_rate):
    phenotype = []
    if local_search_type == "uniform":
        phenotype = uniform_local_search(genotype, genotype_range, num_genes, local_search_rate)
    elif local_search_type == "gaussian":
        phenotype = guass_local_search(genotype, genotype_range, num_genes, local_search_rate)
    elif local_search_type == "hill_climbing":
        phenotype = hill_climbing_local_search(genotype, num_genes, local_search_rate)
    return phenotype
