# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 22:12
import random

import numpy as np


# crossover_type: the type of crossover, it can be 'one-point', 'two-point', 'probabilistic', 'arithmetic', 'linear_combination',"Roulette wheel"
# based on different crossover_type, use different crossover method to crossover two individuals
# crossover_rate is the probability of crossover
# if a random probability is less than crossover_rate, then crossover two individuals, else return one of the two individuals, which is chosen randomly
# algorithm is a parameter, if algorithm="Baseline" or "Baldwin", then use genotypes of two individuals to crossover, elif algorithm="Lamarck", then use phenotypes of two individuals to crossover


def one_point_crossover(individual1, individual2, algorithm):
    # # print corssover method green color
    # print(colorama.Fore.YELLOW + "one point crossover")
    # choose a random point to crossover
    global child1, child2
    crossover_point = np.random.randint(0, len(individual1.genotype) - 1)
    # # print genotype of two individuals and crossover point use color and explaination
    # print(colorama.Fore.BLUE + "crossover point: " + str(crossover_point))
    # print(colorama.Fore.GREEN + "individual1 genotype: " + str(individual1.genotype))
    # print(colorama.Fore.GREEN + "individual2 genotype: " + str(individual2.genotype))
    if algorithm == "Baseline" or algorithm == "Baldwin":
        # crossover genotypes of two individuals
        individual1.genotype[crossover_point:], individual2.genotype[crossover_point:] = individual2.genotype[
                                                                                         crossover_point:], individual1.genotype[
                                                                                                            crossover_point:]
        child1 = individual1.genotype
        child2 = individual2.genotype
    elif algorithm == "Lamarck":
        # crossover phenotypes of two individuals
        individual1.phenotype[crossover_point:], individual2.phenotype[crossover_point:] = individual2.phenotype[
                                                                                           crossover_point:], individual1.phenotype[
                                                                                                              crossover_point:]
        child1 = individual1.phenotype
        child2 = individual2.phenotype
    # if this crossover method create two children, then randomly choose one of them to return
    # print(colorama.Fore.GREEN + "child1: " + str(child1))
    # print(colorama.Fore.GREEN + "child2: " + str(child2))
    return random.choice([child1, child2])


def two_point_crossover(individual1, individual2, algorithm):
    # # print corssover method green color
    # print(colorama.Fore.YELLOW + "two point crossover")
    # choose two random points to crossover
    global child1, child2
    crossover_point1 = random.randint(0, len(individual1.genotype) - 1)
    crossover_point2 = random.randint(0, len(individual1.genotype) - 1)
    if crossover_point1 > crossover_point2:
        crossover_point1, crossover_point2 = crossover_point2, crossover_point1
    # print(colorama.Fore.BLUE + "crossover point1: " + str(crossover_point1))
    # print(colorama.Fore.BLUE + "crossover point2: " + str(crossover_point2))
    # print(individual1.genotype, individual2.genotype)
    if algorithm == "Baseline" or algorithm == "Baldwin":
        # crossover genotypes of two individuals
        individual1.genotype[crossover_point1:crossover_point2], individual2.genotype[
                                                                 crossover_point1:crossover_point2] = individual2.genotype[
                                                                                                      crossover_point1:crossover_point2], individual1.genotype[
                                                                                                                                          crossover_point1:crossover_point2]
        child1 = individual1.genotype
        child2 = individual2.genotype
    elif algorithm == "Lamarck":
        # crossover phenotypes of two individuals
        individual1.phenotype[crossover_point1:crossover_point2], individual2.phenotype[
                                                                  crossover_point1:crossover_point2] = individual2.phenotype[
                                                                                                       crossover_point1:crossover_point2], individual1.phenotype[
                                                                                                                                           crossover_point1:crossover_point2]
        child1 = individual1.phenotype
        child2 = individual2.phenotype
    # if this crossover method create two children, then randomly choose one of them to return
    # use one line code
    # print(colorama.Fore.GREEN + "child1: " + str(child1))
    # print(colorama.Fore.GREEN + "child2: " + str(child2))
    return random.choice([child1, child2])


def probabilistic_crossover(individual1, individual2, algorithm, crossover_rate):
    # print(colorama.Fore.YELLOW + "probabilistic crossover")
    # print(individual1.genotype, individual2.genotype)
    # for each gene in the child, generate a random number between 0 and 1, compare it with crossover_rate, if it is less than crossover_rate, then assign the gene of individual1 to the child, else assign the gene of individual2 to the child
    child = []
    if algorithm == "Baseline" or algorithm == "Baldwin":
        child = [gene1 if np.random.random() < crossover_rate else gene2 for gene1, gene2 in
                 zip(individual1.genotype, individual2.genotype)]
    elif algorithm == "Lamarck":
        child = [gene1 if np.random.random() < crossover_rate else gene2 for gene1, gene2 in
                 zip(individual1.phenotype, individual2.phenotype)]
    # print(colorama.Fore.GREEN + "child: " + str(child))
    return child


def linear_combination_crossover(individual1, individual2, algorithm, crossover_rate):
    # print(colorama.Fore.YELLOW + "linear combination crossover")
    # print(colorama.Fore.GREEN + "individual1 genotype: " + str(individual1.genotype))
    # print(colorama.Fore.GREEN + "individual2 genotype: " + str(individual2.genotype))
    # for each gene in the child, generate a random number between 0 and 1, then calculate the gene of the child by using the formula: gene = alpha * gene1 + (1 - alpha) * gene2
    child = []
    if algorithm == "Baseline" or algorithm == "Baldwin":
        child = [crossover_rate * gene1 + (1 - crossover_rate) * gene2 for gene1, gene2 in
                 zip(individual1.genotype, individual2.genotype)]
    elif algorithm == "Lamarck":
        child = [crossover_rate * gene1 + (1 - crossover_rate) * gene2 for gene1, gene2 in
                 zip(individual1.phenotype, individual2.phenotype)]
    # print(colorama.Fore.GREEN + "child: " + str(child))
    return child


def average(individual1, individual2, algorithm, crossover_rate):
    # print(colorama.Fore.YELLOW + "average crossover")
    # print(colorama.Fore.GREEN + "individual1 genotype: " + str(individual1.genotype))
    # print(colorama.Fore.GREEN + "individual2 genotype: " + str(individual2.genotype))
    child = []
    if algorithm == "Baseline" or algorithm == "Baldwin":
        child = [(gene1 + gene2) * (1 - crossover_rate) / 2 for gene1, gene2 in
                 zip(individual1.genotype, individual2.genotype)]
    elif algorithm == "Lamarck":
        child = [(gene1 + gene2) * (1 - crossover_rate) / 2 for gene1, gene2 in
                 zip(individual1.phenotype, individual2.phenotype)]
    # print(colorama.Fore.GREEN + "child: " + str(child))
    return child


def roulette_wheel_crossover(individual1, individual2, crossover_rate):
    # print(colorama.Fore.YELLOW + "roulette wheel crossover")
    # print(colorama.Fore.GREEN + "individual1 genotype: " + str(individual1.genotype))
    # print(colorama.Fore.GREEN + "individual2 genotype: " + str(individual2.genotype))
    # use roulette wheel to calculate the two probability lists of each gene in individual1 and individual2,
    # for each gene in individual1, the probability of this gene is the value/sum of all values in individual1
    # for each gene, if any of two probabilities is larger than crossover_rate, the child will get a smaller value of the two genes
    # else generate a random value between the two genes,a float number
    # probality list of individual1
    # take the absolute value of each gene in individual1 and then calculate the sum of all genes
    sum1 = sum([abs(gene) for gene in individual1.genotype])
    # calculate the probability of each gene in individual1
    prob1 = [abs(gene) / sum1 for gene in individual1.genotype]
    # probality list of individual2
    sum2 = sum([abs(gene) for gene in individual2.genotype])
    prob2 = [abs(gene) / sum2 for gene in individual2.genotype]
    # # print sum of prob1 and prob2
    # print(colorama.Fore.GREEN + "sum of prob1: " + str(sum(prob1)))
    # print(colorama.Fore.GREEN + "sum of prob2: " + str(sum(prob2)))
    # print(colorama.Fore.BLUE + "prob1: " + str(prob1))
    # print(colorama.Fore.BLUE + "prob2: " + str(prob2))
    # print(crossover_rate)
    child = []
    for i in range(len(individual1.genotype)):
        if prob1[i] > crossover_rate or prob2[i] > crossover_rate:
            child.append(min(individual1.genotype[i], individual2.genotype[i]))
        else:
            child.append(random.uniform(individual1.genotype[i], individual2.genotype[i]))
    # print(colorama.Fore.GREEN + "child: " + str(child))
    return child


def crossover(individual1, individual2, crossover_type, crossover_rate, algorithm):
    if crossover_type == "one-point":
        if np.random.random() < crossover_rate:
            return one_point_crossover(individual1, individual2, algorithm)
        else:
            if algorithm == "Baseline" or algorithm == "Baldwin":
                return random.choice([individual1.genotype, individual2.genotype])
            elif algorithm == "Lamarck":
                return random.choice([individual1.phenotype, individual2.phenotype])

    elif crossover_type == "two-point":
        if random.random() < crossover_rate:
            return two_point_crossover(individual1, individual2, algorithm)
        else:
            if algorithm == "Baseline" or algorithm == "Baldwin":
                return random.choice([individual1.genotype, individual2.genotype])
            elif algorithm == "Lamarck":
                return random.choice([individual1.phenotype, individual2.phenotype])

    elif crossover_type == "Probabilistic_crossover":
        return probabilistic_crossover(individual1, individual2, algorithm, crossover_rate)
    elif crossover_type == "linear combination":
        return linear_combination_crossover(individual1, individual2, algorithm, crossover_rate)
    elif crossover_type == "average":
        return average(individual1, individual2, algorithm, crossover_rate)
    elif crossover_type == "Roulette wheel":
        return roulette_wheel_crossover(individual1, individual2, crossover_rate)
    else:
        print("Error: invalid crossover type")
        return None
