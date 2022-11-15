[TOC]

# Comparing the Lamarckian and Baldwinian Approaches in Memetic Optimization

## Abstract

`Abstract:` Memetic optimization (MO) combines local and global search in optimization in non-monotonic, ‘rugged’ search spaces. In particular, MO extends genetic optimization, where global search is implemented via the crossover operator and local search is performed as random mutation. MO uses more elaborate techniques to implement local search and to combine it with its global counterpart. This study is set to compare two ways of memetic optimization: one motivated by the Baldwinian, while the other by the Lamarckian theory of evolution.

Both the Baldwinian and Lamarckian theory suggest that behaviors of individuals are not only passed on to offspring by crossover and mutation, but also through lifetime learning. In Baldwin approach, learned behaviors affect the mapping of genotypes to phenotypes, which ultimately results in changes to the fitness landscape. In Lamarck approach, not only will the learned behaviors affect the fitness landscape in the same way as the former does, but they will also be passed on to offspring through phenotypes. Whilst the biological plausibility of these perspectives is questionable, they offer a valuable structure for constructing memetic optimization algorithms. 

Before exploring Lamarckian and Baldwinian approaches, a baseline framework where offspring can only inherit the characteristics of the parent through crossover and mutation (i.e., genetic optimization) is considered as a global optimization problem. Based on the baseline framework, we develop various implementations of the Lamarckian and Baldwinian approaches exploring several local search procedures to study the potential contributions of the studied approaches. Our experiments will be performed on the CEC-BC-2017 test functions for optimization.

`Keywords`: Baldwinian evolution; Lamarckian evolution; Memetic optimization; Fitness landscape; Learning; CEC-BC-2017.

## Introduction

## Methods selection

### Terminology 

#### Genotype & Phenotype

#### Fitness Function

#### Probability Crossover

#### Linear Combination Crossover

#### Single Point Crossover

#### Normal Mutation

#### Uniform Mutation

### Steady-state Genetic Algorithm

Steady-state genetic algorithm (SSGA) is implemented as a baseline framework in order to demonstrate the progress and improvements which Lamarckian and Baldwinian approaches provide. SSGA maintains a stable population size by generating only one new offspring based on the best individual in the population, while discarding the least adapted individual. The individual holding the lowest position in the fitness landscape is defined as the best individual, as our goal is to find the global minimum. In contrast, the individuals who are least adapted to the environment have the highest position. For all individuals in SSGA, genotypes and phenotypes are vectors of equal dimensions and equal values at corresponding positions in every test function of CEC-BC-2017. Fitness value of an individual is computed based on its phenotype. The genotypes of the primordial populations are randomly created with every gene located within the domain of a test function. 

#### Flowchat of SSGA

#### Pseudo-code of SSGA

### Baldwinian & Lamarckian Algorithm

#### Flowchat of Baldwin & Lamarck

#### Pseudo-code of Baldwin & Lamarck

## Performance Analysis

### Experiments

### Tables for Comparison

### Max Min Mean STD of Global Minimas/Solutions

### Data visualization for Similarity

### Data visualization for Budget

## Conclusion

## References

## Appendix

