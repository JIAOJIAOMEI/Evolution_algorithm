# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 13:40

import math
import random

import numpy as np

# from sympy import sin, cos, exp, prod, sqrt,pi

power = math.pow
cos = math.cos
sin = math.sin
pi = math.pi
exp = math.exp
sqrt = math.sqrt
e = math.e
prod = math.prod


def F1(x):
    """
        :param x: 1*50
        :return: fitness
        """
    fitness = [power(i, 2) for i in x]
    return sum(fitness)


def F2(x):
    """
    :param x: 1*50
    :return: fitness
    """
    x = [abs(i) for i in x]
    fitness = sum(x) + prod(x)
    return fitness


def F3(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = [power(i, 2) for i in x]
    return 50 * sum(fitness)


def F4(x):
    """
    :param x: 1*50
    :return: fitness
    """
    x = [abs(i) for i in x]
    return max(x)


def F5(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = [100 * power(x[i + 1] - power(x[i], 2), 2) + power(x[i] - 1, 2) for i in range(len(x) - 1)]
    return sum(fitness)


def F6(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = [power(x[i] + 0.5, 2) for i in range(len(x) - 1)]
    return sum(fitness)


def F7(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = [power(x[i], 4) * (i + 1) for i in range(len(x))]
    return sum(fitness)


def F8(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = []
    for i in x:
        k = (-1) * i * sin(sqrt(abs(i)))
        fitness.append(k)
    return sum(fitness)


def F9(x):
    """
    :param x: 1*50
    :return: fitness
    """
    fitness = [power(i, 2) - (10 * cos(2 * pi * i)) + 10 for i in x]
    return sum(fitness)


def F10(x):
    """
    :param x: 1*50
    :return: fitness
    """
    part1 = sum([power(i, 2) for i in x])
    part2 = sum([cos(2 * pi * i) for i in x])
    fitness = (-20) * exp(-0.2 * sqrt(0.02 * part1)) + (-exp(0.02 * part2) + 20 + e)
    return fitness


def F11(x):
    """
    :param x: 1*50
    :return: fitness
    """
    part1 = sum([power(i, 2) for i in x])
    part2 = prod([cos(x[i] / sqrt(i + 1)) for i in range(len(x))])
    fitness = part1 / 4000 - part2 + 1
    return fitness


def U(x, a, k, m):
    '''
    :param x:
    :param a:
    :param k:
    :param m:
    :return:
    '''
    if x > a:
        u = k * power(x - a, m)
    elif x < (-a):
        u = k * power(-x - a, m)
    else:
        u = 0
    return u


def F12(x):
    """
    :param x: 1*50
    :return: fitness
    """
    y = [1 + (i + 1) / 4 for i in x]
    part3 = sum([U(i, 10, 100, 4) for i in x])
    part2 = sum([power(y[i] - 1, 2) * (1 + 10 * power(sin(y[i + 1] * pi), 2)) for i in range(len(x) - 1)])
    fitness = (pi / 50) * (10 * power(sin(y[0] * pi), 2) + part2 + power(y[-1] - 1, 2)) + part3
    return fitness


def F13(x):
    """
    :param x: 1*50
    :return: fitness
    """
    part2 = sum([power(x[i] - 1, 2) * (1 + power(sin(3 * pi * x[i]) + 1, 2)) for i in range(len(x) - 1)])
    part3 = power(x[-1] - 1, 2) * (1 + power(sin(2 * pi * x[-1]), 2))
    part4 = sum([U(i, 5, 100, 4) for i in x])
    fitness = 0.1 * (power(sin(3 * pi * x[0]), 2) + part2 + part3) + part4
    return fitness


def F14(x):
    """
    :param x: 1*2
    :return: fitness
    """
    a = [[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
         [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]]
    part2 = []
    for j in range(25):
        k = power(j + 1 + sum([power(x[i] - a[i][j], 6) for i in range(2)]), -1)
        part2.append(k)
    fitness = power(1 / 500 + sum(part2), -1)
    return fitness


def F15(x):
    """
    :param x: 1*4
    :return: fitness
    """
    a = [.1957, .1947, .1735, .16, .0844, .0627, .0456, .0342, .0323, .0235, .0246]
    b = [.25, .5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
    b = [1 / i for i in b]
    fitness = sum([power(a[i] - ((x[0] * (power(b[i], 2) + b[i] * x[1])) / (
            power(b[i], 2) + b[i] * x[2] + x[3])), 2) for i in range(11)])
    return fitness


def F16(x):
    """
    :param x: 1*2
    :return: fitness
    """
    x1 = x[0]
    x2 = x[1]
    fitness = 4 * power(x1, 2) - 2.1 * power(x1, 4) + (1 / 3) * power(x1, 6) + x1 * x2 - 4 * power(x2, 2) + 4 * power(
        x2, 4)
    return fitness


def F17(x):
    """
    :param x: 1*2
    :return: fitness
    """
    x1 = x[0]
    x2 = x[1]
    fitness = power(x2 - 5.1 / (4 * power(pi, 2)) * power(x1, 2) + 5 / pi * x1 - 6, 2) + 10 * (
            1 - (1 / (8 * pi))) * cos(x1) + 10
    return fitness


def F18(x):
    """
    :param x: 1*2
    :return: fitness
    """
    x1 = x[0]
    x2 = x[1]
    part1 = 1 + power(x1 + x2 + 1, 2) * (19 - 14 * x1 + 3 * power(x1, 2) - 14 * x2 + 6 * x1 * x2 + 3 * power(x2, 2))
    part2 = 30 + power(2 * x1 - 3 * x2, 2) * (
            18 - 32 * x1 + 12 * power(x1, 2) + 48 * x2 - 36 * x1 * x2 + 27 * power(x2, 2))
    fitness = part1 * part2
    return fitness


def F19(x):
    """
    :param x: 1*3
    :return: fitness
    """
    a = [[3, 10, 30], [.1, 10, 35], [3, 10, 30], [.1, 10, 35]]
    c = [1, 1.2, 3, 3.2]
    p = [[.3689, .117, .2673], [.4699, .4387, .747], [.1091, .8732, .5547], [.03815, .5743, .8828]]
    fitness = []
    for i in range(4):
        inner_part = -sum([a[i][j] * power(x[j] - p[i][j], 2) for j in range(3)])
        fitness.append(c[i] * exp(inner_part))
    return -sum(fitness)


def F20(x):
    """
    :param x: 1*6
    :return: fitness
    """
    a = [[10, 3, 17, 3.5, 1.7, 8], [.05, 10, 17, .1, 8, 14], [3, 3.5, 1.7, 10, 17, 8], [17, 8, .05, 10, .1, 14]]
    c = [1, 1.2, 3, 3.2]
    p = [[.1312, .1696, .5569, .0124, .8283, .5886], [.2329, .4135, .8307, .3736, .1004, .9991],
         [.2348, .1415, .3522, .2883, .3047, .6650], [.4047, .8828, .8732, .5743, .1091, .0381]]
    fitness = []
    for i in range(4):
        inner_part = -sum([a[i][j] * power(x[j] - p[i][j], 2) for j in range(6)])
        fitness.append(c[i] * exp(inner_part))
    return -sum(fitness)


def F21(x):
    """
    :param x: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7]]
    c = [.1, .2, .2, .4, .4]
    fitness = []

    for i in range(5):
        inner = power(np.dot(np.array([x[k] - a[i][k] for k in range(4)]),
                             np.array([x[k] - a[i][k] for k in range(4)]).T) + c[i], -1)
        fitness.append(inner)
    return -sum(fitness)


def F22(x):
    """
    :param x: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3]]
    c = [.1, .2, .2, .4, .4, .6, .3]
    fitness = []
    for i in range(7):
        inner = power(np.dot(np.array([x[k] - a[i][k] for k in range(4)]),
                             np.array([x[k] - a[i][k] for k in range(4)]).T) + c[i], -1)
        fitness.append(inner)
    return -sum(fitness)


def F23(x):
    """
    :param x: 1*4
    :return: fitness
    """
    a = [[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1],
         [6, 2, 6, 2], [7, 3.6, 7, 3.6]]
    c = [.1, .2, .2, .4, .4, .6, .3, .7, .5, .5]
    fitness = []
    for i in range(10):
        inner = power(np.dot(np.array([x[k] - a[i][k] for k in range(4)]),
                             np.array([x[k] - a[i][k] for k in range(4)]).T) + c[i], -1)
        fitness.append(inner)
    return -sum(fitness)

