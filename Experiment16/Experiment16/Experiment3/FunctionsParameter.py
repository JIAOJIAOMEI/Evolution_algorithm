# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 1/1/23 20:19
import TestFunctions


def get_functions_parameter(function, flexible_dimensions=50):
    func = None
    num_genes = None
    genotype_range = None
    if function == 1:
        func = TestFunctions.F1
        num_genes = flexible_dimensions
        genotype_range = [-100, 100]
    elif function == 2:
        func = TestFunctions.F2
        num_genes = flexible_dimensions
        genotype_range = [-100, 100]
    elif function == 3:
        func = TestFunctions.F3
        num_genes = flexible_dimensions
        genotype_range = [-100, 100]
    elif function == 4:
        func = TestFunctions.F4
        num_genes = flexible_dimensions
        genotype_range = [-100, 100]
    elif function == 5:
        func = TestFunctions.F5
        num_genes = flexible_dimensions
        genotype_range = [-30, 30]
    elif function == 6:
        func = TestFunctions.F6
        num_genes = flexible_dimensions
        genotype_range = [-100, 100]
    elif function == 7:
        func = TestFunctions.F7
        num_genes = flexible_dimensions
        genotype_range = [-1.28, 1.28]
    elif function == 8:
        func = TestFunctions.F8
        num_genes = flexible_dimensions
        genotype_range = [-500, 500]
    elif function == 9:
        func = TestFunctions.F9
        num_genes = flexible_dimensions
        genotype_range = [-5.12, 5.12]
    elif function == 10:
        func = TestFunctions.F10
        num_genes = flexible_dimensions
        genotype_range = [-32, 32]
    elif function == 11:
        func = TestFunctions.F11
        num_genes = flexible_dimensions
        genotype_range = [-600, 600]
    elif function == 12:
        func = TestFunctions.F12
        num_genes = flexible_dimensions
        genotype_range = [-50, 50]
    elif function == 13:
        func = TestFunctions.F13
        num_genes = flexible_dimensions
        genotype_range = [-50, 50]
    elif function == 14:
        func = TestFunctions.F14
        num_genes = 2
        genotype_range = [-65, 65]
    elif function == 15:
        func = TestFunctions.F15
        num_genes = 4
        genotype_range = [-5, 5]
    elif function == 16:
        func = TestFunctions.F16
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 17:
        func = TestFunctions.F17
        num_genes = 2
        genotype_range = [-5, 5]
    elif function == 18:
        func = TestFunctions.F18
        num_genes = 2
        genotype_range = [-2, 2]
    elif function == 19:
        func = TestFunctions.F19
        num_genes = 3
        genotype_range = [0, 1]
    elif function == 20:
        func = TestFunctions.F20
        num_genes = 6
        genotype_range = [0, 1]
    elif function == 21:
        func = TestFunctions.F21
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 22:
        func = TestFunctions.F22
        num_genes = 4
        genotype_range = [0, 10]
    elif function == 23:
        func = TestFunctions.F23
        num_genes = 4
        genotype_range = [0, 10]
    return func, num_genes, genotype_range
