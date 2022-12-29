# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:17
import improved_fitness_functions


def choose_func(function):
    func = None
    num_genes = None
    genotype_range = None
    if function == 1:
        func = improved_fitness_functions.F1
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 2:
        func = improved_fitness_functions.F2
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 3:
        func = improved_fitness_functions.F3
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 4:
        func = improved_fitness_functions.F4
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 5:
        func = improved_fitness_functions.F5
        num_genes = 50
        genotype_range = [-30, 30]
    elif function == 6:
        func = improved_fitness_functions.F6
        num_genes = 50
        genotype_range = [-100, 100]
    elif function == 7:
        func = improved_fitness_functions.F7
        num_genes = 50
        genotype_range = [-1.28, 1.28]
    elif function == 8:
        func = improved_fitness_functions.F8
        num_genes = 50
        genotype_range = [-500, 500]
    elif function == 9:
        func = improved_fitness_functions.F9
        num_genes = 50
        genotype_range = [-5.12, 5.12]
    elif function == 10:
        func = improved_fitness_functions.F10
        num_genes = 50
        genotype_range = [-32, 32]
    elif function == 11:
        func = improved_fitness_functions.F11
        num_genes = 50
        genotype_range = [-600, 600]
    elif function == 12:
        func = improved_fitness_functions.F12
        num_genes = 50
        genotype_range = [-50, 50]
    elif function == 13:
        func = improved_fitness_functions.F13
        num_genes = 50
        genotype_range = [-50, 50]
    elif function == 14:
        func = improved_fitness_functions.F14
        num_genes = 2
        genotype_range = [-65, 65]
    elif function == 15:
        func = improved_fitness_functions.F15
        num_genes = 4
        genotype_range = [-5, 5]
    elif function == 16:
        func = improved_fitness_functions.F16
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 17:
        func = improved_fitness_functions.F17
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 18:
        func = improved_fitness_functions.F18
        num_genes = 2
        genotype_range = [-2, 2]
    elif function == 19:
        func = improved_fitness_functions.F19
        num_genes = 3
        genotype_range = [1, 3]
    elif function == 20:
        func = improved_fitness_functions.F20
        num_genes = 6
        genotype_range = [0, 1]
    elif function == 21:
        func = improved_fitness_functions.F21
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 22:
        func = improved_fitness_functions.F22
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 23:
        func = improved_fitness_functions.F23
        num_genes = 4
        genotype_range = [0, 10]
    return func, num_genes, genotype_range
