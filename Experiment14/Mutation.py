# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 20:56
from random import random

import numpy as np


# parameters: mutation_type, mutation_rate, the child of two individuals, genotype_range, num_genes,search_radius
# create multiple methods based on mutation_type,it can be 'uniform', 'gaussian',"frequency-based"
# mutation_rate: the probability of mutation, a float number between 0 and 1，
# the child of two individuals: the child to be mutated
# genotype_range: the range of the genes in the individual, which is the range of the function, a list with two elements, the first is the lower bound, the second is the upper bound
# if mutation_type is 'uniform', then use uniform mutation
# if mutation_type is 'gaussian', then use gaussian mutation, loc=0, std=mutation_range/6
# if mutation_type is 'frequency-based', then use frequency-based mutation, the frequency of mutation is determined by the frequency of the gene in the population, the more frequent the gene is, the less likely it is to be mutated, and vice versa，when calculating the frequency of the gene, the gene is divided into 10 categories, and the frequency of each category is calculated,each category is a list with two elements, the first is the lower bound of the category, the second is the upper bound of the category, the frequency of the gene is the number of genes in the category divided by the total number of genes，after get the 10 categories, calculate the probability of mutation for each gene, the probability of mutation is 1 - frequency of the gene，if the probability of mutation is greater than the mutation_rate, then mutate the gene.
# search_radius: a float number, use search_radius*genotype_range=mutation_range to get the range of the mutation,search_radius is a Individual parameter
# make sure that the mutated child is within the range of genotype_range
# if a gene is going to be mutated,then generate a random variable within the range of mutation_range, and add it to the gene
# mutation_range = search_radius * genotype_range, a list with two elements, the first is the lower bound, the second is the upper bound
# return the mutated child


def uniform_mutation(mutation_rate, child, genotype_range, num_genes, search_radius):
    mutation_range = [search_radius * genotype_range[0], search_radius * genotype_range[1]]
    # print(num_genes)
    # print(len(child))
    for i in range(num_genes):
        if random() < mutation_rate:
            child[i] = child[i] + np.random.uniform(mutation_range[0], mutation_range[1])
            # check if the child is within the range of genotype_range use max and min function
            child[i] = max(child[i], genotype_range[0])
            child[i] = min(child[i], genotype_range[1])
    return child


def guassian_mutation(mutation_rate, child, genotype_range, num_genes, search_radius):
    mutation_range = [search_radius * genotype_range[0], search_radius * genotype_range[1]]
    for i in range(num_genes):
        if random() < mutation_rate:
            child[i] = child[i] + np.random.normal(loc=0, scale=(mutation_range[1] - mutation_range[0]) / 6)
            # check if the child is within the range of genotype_range use max and min function
            child[i] = max(child[i], genotype_range[0])
            child[i] = min(child[i], genotype_range[1])
    return child


import colorama


def frequency_based_mutation(mutation_rate, child, genotype_range, num_genes, search_radius):
    mutation_range = [search_radius * genotype_range[0], search_radius * genotype_range[1]]
    # calculate the frequency of each gene
    # divide the genes into 10 categories
    categories = []
    # category_range = max of the gene in the child - min of the gene in the child
    category_range = (max(child) - min(child)) / 10
    for i in range(10):
        categories.append([min(child) + i * category_range, min(child) + (i + 1) * category_range])
    # calculate the frequency of each category
    category_frequency = []
    # print(categories)
    # print(colorama.Fore.RED + 'category frequency: ' + str(categories))
    for i in range(10):
        count = 0
        for j in range(num_genes):
            if categories[i][0] <= child[j] < categories[i][1]:
                count += 1
        category_frequency.append(count / num_genes)
    # print(colorama.Fore.RED + 'category frequency: ' + str(category_frequency))
    # rewrite the code for probability_of_mutation, check the first and last category separately, and then check the other categories
    probability_of_mutation = []
    minimum = min(child)
    for i in range(num_genes):
        # check the first category
        if child[i] < categories[0][1]:
            probability_of_mutation.append(1 - category_frequency[0])
        # check the last category
        elif child[i] >= categories[9][0]:
            probability_of_mutation.append(1 - category_frequency[9])
        # check the other categories
        else:
            probability_of_mutation.append(1 - category_frequency[int(np.floor((child[i] - minimum) / category_range))])
    # print(colorama.Fore.RED + 'probability of mutation: ' + str(probability_of_mutation))
    # mutate the gene
    for i in range(num_genes):
        if probability_of_mutation[i] > mutation_rate:
            child[i] = child[i] + np.random.uniform(mutation_range[0], mutation_range[1])
            # check if the child is within the range of genotype_range use max and min function
            child[i] = max(child[i], genotype_range[0])
            child[i] = min(child[i], genotype_range[1])
    return child


# create a function to choose the mutation method
def mutation(mutation_type, mutation_rate, child, genotype_range, num_genes, search_radius):
    if mutation_type == 'uniform':
        return uniform_mutation(mutation_rate, child, genotype_range, num_genes, search_radius)
    elif mutation_type == 'gaussian':
        return guassian_mutation(mutation_rate, child, genotype_range, num_genes, search_radius)
    elif mutation_type == 'frequency-based':
        return frequency_based_mutation(mutation_rate, child, genotype_range, num_genes, search_radius)
    else:
        print('mutation_type is not valid')
        return None
