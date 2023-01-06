# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/2/23 00:32
import random
import colorama
import numpy as np


def evolution_loop(algorithm_parameters):
    # get all the parameters from the class
    num_generations = algorithm_parameters.num_generations
    mutation_rate = algorithm_parameters.mutation_rate
    num_individuals = algorithm_parameters.num_individuals
    crossover_rate = algorithm_parameters.crossover_rate
    mutation_type = algorithm_parameters.mutation_type
    crossover_type = algorithm_parameters.crossover_type
    local_search_rate = algorithm_parameters.local_search_rate
    local_search_type = algorithm_parameters.local_search_type
    search_radius = algorithm_parameters.search_radius
    num_evaluations = algorithm_parameters.num_evaluations
    func = algorithm_parameters.func
    num_genes = algorithm_parameters.num_genes
    genotype_range = algorithm_parameters.genotype_range
    gg = algorithm_parameters.gg
    selection_method = algorithm_parameters.selection_method
    algorithm = algorithm_parameters.algorithm
    # create a list to store the best fitness value of each generation
    best_fitness_list = []
    # set a counter to count the number of evaluations
    num_evaluations_counter = 0
    # set a counter to count the number of generations
    num_generations_counter = 0
    # initialize the population
    # create an initial population by calling the function create_individuals in CreateIndividuals.py
    from CreateIndividuals import create_individuals
    population = create_individuals(population_size=num_individuals, func=func, num_genes=num_genes,
                                    genotype_range=genotype_range, mutation_rate=mutation_rate,
                                    crossover_rate=crossover_rate, mutation_type=mutation_type,
                                    crossover_type=crossover_type, search_radius=search_radius, algorithm=algorithm,
                                    local_search_type=local_search_type, local_search_rate=local_search_rate,
                                    genotype=None)
    # print the length of initial population
    # print(colorama.Fore.RED + "The length of initial population is: " + str(len(population)))
    # selection
    from SelectParents import selection
    # one line code : create empyty to store eligible_individuals, eligible_partners, non_eligible_individuals
    eligible_individuals, eligible_partners, non_eligible_individuals = selection(individuals=population, gg=gg,
                                                                                  selection_method=selection_method)
    # print(colorama.Fore.GREEN + "Eligible individuals: " + str(eligible_individuals))
    # print genotyoe and phenotype of eligible individuals
    # for i in range(len(eligible_individuals)):
    #     print(colorama.Fore.GREEN + "The genotype of eligible individual " + str(i) + " is: " + str(
    #         eligible_individuals[i].genotype))
    #     print(colorama.Fore.GREEN + "The phenotype of eligible individual " + str(i) + " is: " + str(
    #         eligible_individuals[i].phenotype))
    # print(colorama.Fore.GREEN + "Eligible partners: " + str(eligible_partners))
    # print(colorama.Fore.GREEN + "Non-eligible individuals: " + str(non_eligible_individuals))
    # for each individual in eligible_individuals, find a partner in eligible_partners
    # and then do cross over and mutation
    from Crossover import crossover
    from Mutation import mutation
    new_individuals = []
    for individual in eligible_individuals:
        # find a partner
        partner = np.random.choice(eligible_partners,replace=True)
        # print(colorama.Fore.GREEN + "Individual: " + str(individual))
        # print(colorama.Fore.GREEN + "Partner: " + str(partner))
        child = crossover(individual1=individual, individual2=partner, crossover_type=crossover_type,
                          crossover_rate=crossover_rate, algorithm=algorithm)
        # print(colorama.Fore.GREEN + "Child: " + str(child))
        child = mutation(mutation_type=mutation_type, mutation_rate=mutation_rate, child=child,
                         genotype_range=genotype_range, num_genes=num_genes, search_radius=search_radius)
        # child is a list of genes, use it as a genotype to create a new individual
        from CreateIndividuals import Individual
        new_individual = Individual(func=func, num_genes=num_genes, genotype_range=genotype_range,
                                    mutation_rate=mutation_rate,
                                    crossover_rate=crossover_rate, mutation_type=mutation_type,
                                    crossover_type=crossover_type,
                                    search_radius=search_radius, algorithm=algorithm,
                                    local_search_type=local_search_type,
                                    local_search_rate=local_search_rate, genotype=child)
        # create a list to store the new individuals
        new_individuals.append(new_individual)
        # print length of new individuals
    # print(colorama.Fore.RED + "The length of new individuals is: " + str(len(new_individuals)))
    # delete the non_eligible_individuals from the population
    for individual in non_eligible_individuals:
        population.remove(individual)
    # the individuals are soeted in the population, the lower the fitness, the lower the rank
    # now insert the new individuals into the population based on their fitness and update the ranks
    # for each new individual, find the position to insert it into the population
    for new_individual in new_individuals:
        for i in range(len(population)):
            if new_individual.fitness < population[i].fitness:
                population.insert(i, new_individual)
                break
            else:
                population.append(new_individual)
                break
    # update the ranks of the individuals in the population
    for i in range(len(population)):
        population[i].rank = i + 1
    best_fitness_list.append(population[0].fitness)
    num_generations_counter += 1
    if algorithm == "Baseline":
        if crossover_type != "SSGA":
            num_evaluations_counter += num_individuals + 1
        else:
            num_evaluations_counter += num_individuals + int(gg * len(population))
    else:
        num_evaluations_counter += 2 * (num_individuals + int(gg * len(population)))

    # start the evolution loop
    while num_generations_counter < num_generations and num_evaluations_counter < num_evaluations:
        # selection
        eligible_individuals, eligible_partners, non_eligible_individuals = selection(individuals=population, gg=gg,
                                                                                      selection_method=selection_method)
        # print(colorama.Fore.BLUE + "Now we are in the loop")
        # print(colorama.Fore.BLUE + "Eligible individuals: " + str(len(eligible_individuals)))
        # print(colorama.Fore.BLUE + "Eligible partners: " + str(len(eligible_partners)))
        # print(colorama.Fore.BLUE + "Non-eligible individuals: " + str(len(non_eligible_individuals)))
        # for each individual in eligible_individuals, find a partner in eligible_partners
        # and then do cross over and mutation
        new_individuals = []
        for individual in eligible_individuals:
            # find a partner
            # print length of population
            # print(colorama.Fore.RED + "Length of population: " + str(len(population)))
            partner = np.random.choice(eligible_partners,replace=True)
            # print length of eligible_partners
            # print(colorama.Fore.RED + "Length of eligible partners: " + str(len(eligible_partners)))
            child = crossover(individual1=individual, individual2=partner, crossover_type=crossover_type,
                              crossover_rate=crossover_rate, algorithm=algorithm)
            child = mutation(mutation_type=mutation_type, mutation_rate=mutation_rate, child=child,
                             genotype_range=genotype_range, num_genes=num_genes, search_radius=search_radius)
            # child is a list of genes, use it as a genotype to create a new individual
            from CreateIndividuals import Individual
            new_individual = Individual(func=func, num_genes=num_genes, genotype_range=genotype_range,
                                        mutation_rate=mutation_rate,
                                        crossover_rate=crossover_rate, mutation_type=mutation_type,
                                        crossover_type=crossover_type,
                                        search_radius=search_radius, algorithm=algorithm,
                                        local_search_type=local_search_type,
                                        local_search_rate=local_search_rate, genotype=child)
            # create a list to store the new individuals
            new_individuals.append(new_individual)
        # delete the non_eligible_individuals from the population,one line code
        # print(colorama.Fore.RED + "Length of population before deletion: " + str(len(population)))
        population = [individual for individual in population if individual not in non_eligible_individuals]
        # print length of population
        # print(colorama.Fore.RED + "Length of population after deletion: " + str(len(population)))
        # the individuals are soeted in the population, the lower the fitness, the lower the rank
        # now insert the new individuals into the population based on their fitness and update the ranks
        # for
        for new_individual in new_individuals:
            for i in range(len(population)):
                if new_individual.fitness < population[i].fitness:
                    population.insert(i, new_individual)
                    break
                else:
                    population.append(new_individual)
                    break
        # update the ranks of the individuals in the population
        # print(colorama.Fore.RED + "The length of new individuals is: " + str(len(new_individuals)))
        for i in range(len(population)):
            population[i].rank = i + 1
        best_fitness_list.append(population[0].fitness)
        num_generations_counter += 1
        if algorithm == "Baseline":
            if crossover_type != "SSGA":
                num_evaluations_counter += num_individuals + 1
            else:
                num_evaluations_counter += num_individuals + int(gg * len(population))
        else:
            num_evaluations_counter += 2 * (num_individuals + int(gg * len(population)))
    # after the evolution loop, return the minimum fitness
    return min(best_fitness_list)
