# Name: Mei Jiaojiao
# Specilization: Artificial Intelligence
# Time and date: 7/25/22 14:16

import numpy as np
import random


def f1(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in individual:
        fitness.append(i ** 2)
    return sum(fitness)


def f2(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in individual:
        fitness.append(abs(i))
    part1 = sum(fitness)
    part2 = np.prod(fitness)
    part2 = np.round(part2,2)
    return part1+part2


def f3(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    length = len(individual)
    for i in individual:
        fitness.append(i ** 2)
    return length * sum(fitness)


def f4(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in individual:
        fitness.append(abs(i))
    return np.max(fitness)


def f5(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in range(len(individual) - 1):
        k = 100 * ((individual[i + 1] - individual[i] ** 2) ** 2) + (individual[i] - 1) ** 2
        fitness.append(k)
    return sum(fitness)


def f6(individual):
    """
    :param individual: 1*49
    :return: fitness
    """
    fitness = []
    for i in individual:
        fitness.append((i + 0.5) ** 2)
    return sum(fitness)


def f7(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in range(len(individual)):
        m = np.round(individual[i] ** 4, 2)
        k = (i+1) * m + random.choice([0, 1])
        fitness.append(k)
    return sum(fitness)


def f8(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in individual:
        k = (-1) * i * np.sin(np.sqrt(abs(i)))
        fitness.append(k)
    return sum(fitness)


def f9(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    fitness = []
    for i in individual:
        k = i ** 2 - (10 * np.cos(2 * np.pi * i) + 10)
        fitness.append(k)
    return sum(fitness)


def f10(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    part1 = sum([i ** 2 for i in individual])
    part2 = sum([np.cos(2 * np.pi * i) for i in individual])
    fitness = (-20) * np.exp(-0.2 * np.sqrt(0.02 * part1)) - np.exp(0.02 * part2) + 20 + np.e
    return fitness


def f11(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    part1 = sum([i ** 2 for i in individual])
    part2 = np.prod([np.cos(individual[i] / np.sqrt(i + 1)) for i in range(len(individual))])
    fitness = part1 / 4000 - part2 + 1
    return fitness


def f12(individual):
    pass


def U(x, a, k, m):
    '''
    :param x:
    :param a:
    :param k:
    :param m:
    :return:
    '''
    if x > a:
        u = k * ((x - a) ** m)
    elif x < (-a):
        u = k * ((-x - a) ** m)
    else:
        u = 0
    return u


def f13(individual):
    """
    :param individual: 1*50
    :return: fitness
    """
    part2 = sum([((i - 1) ** 2) * (1 + np.square(np.sin(3 * np.pi * i + 1))) for i in individual[:-1]])
    part3 = ((individual[-1] - 1) ** 2) * (1 + np.square(np.sin(2 * np.pi * individual[-1])))
    part4 = sum([U(i, 5, 100, 4) for i in individual])
    return 0.1 * (np.square(np.sin(3 * np.pi * individual[0])) + part2 + part3) + part4


def f14(individual):
    """
    :param individual: 1*2
    :return: fitness
    """
    a = [[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
         [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]]
    part2 = []
    for j in range(1, 26):
        k = 1 / (j + sum([(individual[i - 1] - a[i - 1][j - 1]) ** 6 for i in range(1, 3, 1)]))
        part2.append(k)
    fitness = 1 / (1 / 500 + sum(part2))
    return fitness


def f15(individual):
    """
    :param individual: 1*4
    :return: fitness
    """
    a = [.1957, .1947, .1735, .16, .0844, .0627, .0456, .0342, .0323, .0235, .0246]
    b = [.25, .5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
    b = [1 / i for i in b]
    k = sum([np.square(a[i] - ((individual[0] * (b[i] ** 2 + b[i] * individual[1])) / (
            b[i] ** 2 + b[i] * individual[2] + individual[3]))) for i in range(len(a))])
    return k


def f16(individual):
    """
    :param individual: 1*2
    :return: fitness
    """
    x1 = individual[0]
    x2 = individual[1]
    part4 = np.round(4*(x2**4), 2)
    return 4 * (x1 ** 2) - np.round(2.1 * (x1 ** 4), 2) + np.round((1 / 3) * (x1 ** 6), 2) + x1 * x2 - np.round(
        4 * (x2 ** 2), 2) + part4


def f17(individual):
    """
    :param individual: 1*2
    :return: fitness
    """
    x1 = individual[0]
    x2 = individual[1]
    return np.square(x2 - (5.1 / (4 * (np.pi ** 2))) * (x1 ** 2) + (5 / np.pi) * x1 - 6) + 10 * (
            1 - (1 / (8 * np.pi))) * np.cos(x1) + 10


def f18(individual):
    """
    :param individual: 1*2
    :return: fitness
    """
    x1 = individual[0]
    x2 = individual[1]
    part1 = 1 + np.round(((x1 + x2 + 1) ** 2), 2) * np.round(
        (19 - 14 * x1 + 3 * (x1 ** 2) - 14 * x2 + 6 * x1 * x2 + 3 * (x2 ** 2)), 2)
    part2 = 30 + np.round(((2 * x1 - 3 * x2) ** 2), 2) * np.round(
        (18 - 32 * x1 + 12 * (x1 ** 2) + 48 * x2 - 36 * x1 * x2 + 27 * (x2 ** 2)), 2)
    return part1 * part2


def f19(individual):
    """
    :param individual: 1*3
    :return: fitness
    """
    a = [[3, 10, 30], [.1, 10, 35], [3, 10, 30], [.1, 10, 35]]
    c = [1, 1.2, 3, 3.2]
    p = [[.3689, .117, .2673], [.4699, .4387, .747], [.1091, .8732, .5547], [.03815, .5743, .8828]]
    fitness = []
    for i in range(4):
        inner_part = -sum([a[i][j] * (individual[j] - p[i][j]) ** 2 for j in range(3)])
        fitness.append(c[i] * np.exp(inner_part))
    return -sum(fitness)


def f20(individual):
    """
    :param individual: 1*6
    :return: fitness
    """
    a = [[10, 3, 17, 3.5, 1.7, 8], [.05, 10, 17, .1, 8, 14], [3, 3.5, 1.7, 10, 17, 8], [17, 8, .05, 10, .1, 14]]
    c = [1, 1.2, 3, 3.2]
    p = [[.1312, .1696, .5569, .0124, .8283, .5886], [.2329, .4135, .8307, .3736, .1004, .9991],
         [.2348, .1415, .3522, .2883, .3047, .6650], [.4047, .8828, .8732, .5743, .1091, .0381]]
    fitness = []
    for i in range(4):
        inner_part = -sum([a[i][j] * (individual[j] - p[i][j]) ** 2 for j in range(6)])
        fitness.append(c[i] * np.exp(inner_part))
    return -sum(fitness)


def f21(individual):
    """
    :param individual: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7]]
    c = [.1, .2, .2, .4, .4]
    fitness = []
    for i in range(5):
        inner = 1 / (np.dot(np.array([individual[k] - a[i][k] for k in range(4)]),
                            np.array([individual[k] - a[i][k] for k in range(4)]).reshape(4, 1)) + c[i])
        fitness.append(c[i] * np.exp(inner))
    return -sum(fitness)


def f22(individual):
    """
    :param individual: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3]]
    c = [.1, .2, .2, .4, .4, .6, .3]
    fitness = []
    for i in range(7):
        inner = 1 / (np.dot(np.array([individual[k] - a[i][k] for k in range(4)]),
                            np.array([individual[k] - a[i][k] for k in range(4)]).reshape(4, 1)) + c[i])
        fitness.append(c[i] * np.exp(inner))
    return -sum(fitness)


def f23(individual):
    """
    :param individual: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1],
         [6, 2, 6, 2], [7, 3.6, 7, 3.6]]
    c = [.1, .2, .2, .4, .4, .6, .3, .7, .5, .5]
    fitness = []
    for i in range(10):
        inner = 1 / (np.dot(np.array([individual[k] - a[i][k] for k in range(4)]),
                            np.array([individual[k] - a[i][k] for k in range(4)]).reshape(4, 1)) + c[i])
        fitness.append(c[i] * np.exp(inner))
    return -sum(fitness)
