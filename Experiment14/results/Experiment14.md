[TOC]



# performance of parameters

## Stopping conditions

3 stopping conditions in total:

- max number of iterations is reached(for this time, number of iterations is 2000.)
- max number of evaluations is reached(for this time, number of evaluations is 2000.)
- if the sum of fitnesses of phenotypes in all the population does not change in continous 20 iterations, then stop. (The threshold for defining "not change" is 0.0001)

## Mutation rate

The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the values we tried for parameter mutation rate. The y axis is the average/mean of 10 solutions produced by each parameter combination.

![mutation_rate](mutation_rate.png)

# best 20 parameter combinations

```python
num_generations = [2000]
mutation_rate = [0.2, 0.8]
num_individuals = [200]
crossover_rate = [0.2, 0.8]
mutation_type = ["uniform", "gaussian", "frequency_based"]  
crossover_type = ["one-point", "two-point", "probabilistic", "linear combination","average"] 
local_search_rate = [0.2, 0.8]
local_search_type = ["uniform", "gaussian"]  
search_radius = [0.01, 0.1]
num_evaluations = [2000]
threshold = [0.0001]
gg = [0.01, 0.2, 0.5, 0.8, 0.99]
dimensions = [50, 400]
selection_method = ["SSGA", "sorted_selection_part", "sorted_selection_all","roulette_Wheel_Select"]  
fitness_function = [1, 8, 12, 15, 20, 21]
algorithm = ["Baseline", "Lamarck", "Baldwin"]  
```

There are 345,600 parameter combinations in total. Each parameter combination will be run 10 times.

The following shows the process of choosing best 20 parameter combinations, same as previous choosing method: 

A test function is also a parameter. So 345,600/(6 functions) = 57600 unique parameter combinations.

1. Based on the final 10 solutions(10 times run, take the average/mean) produced by one parameter combiantion, get the ranking of the parameter combiantion. The lower the average of 10 sulotions, the higher the ranking. For each function, we have 57600 parameter combinations, then we have a ranking list of 57600.
2. Sum the ranking of F1, F8 and F12 according to the index of a parameter combination. Because only these 3 tested functions' dimensions are flexible. This means the number of dimensions can be increased from 1 to N. 
3. Among all the parameter combinations, find the most smallest 20 sum of rankings where the parameter algorithm is "Baseline".

Result:

|       | num_generations | mutation_rate | num_individuals | crossover_rate |  mutation_type  | crossover_type | local_search_rate | local_search_type | search_radius | num_evaluations | threshold |  gg  | dimensions |   selection_method    | algorithm |
| :---: | :-------------: | :-----------: | :-------------: | :------------: | :-------------: | :------------: | :---------------: | :---------------: | :-----------: | :-------------: | :-------: | :--: | :--------: | :-------------------: | :-------: |
| 18807 |      2000       |      0.2      |       200       |      0.8       |     uniform     |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.8  |    400     | sorted_selection_part | Baseline  |
| 23154 |      2000       |      0.2      |       200       |      0.8       |    gaussian     |    average     |        0.2        |      uniform      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_all  | Baseline  |
| 52431 |      2000       |      0.8      |       200       |      0.8       |    gaussian     |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 56946 |      2000       |      0.8      |       200       |      0.8       | frequency_based |    average     |        0.2        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.5  |    400     | sorted_selection_all  | Baseline  |
| 28431 |      2000       |      0.2      |       200       |      0.8       | frequency_based |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 23562 |      2000       |      0.2      |       200       |      0.8       |    gaussian     |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.2  |    400     | sorted_selection_all  | Baseline  |
| 57207 |      2000       |      0.8      |       200       |      0.8       | frequency_based |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.8  |    400     | sorted_selection_part | Baseline  |
| 23271 |      2000       |      0.2      |       200       |      0.8       |    gaussian     |    average     |        0.2        |      uniform      |      0.1      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 57231 |      2000       |      0.8      |       200       |      0.8       | frequency_based |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 47583 |      2000       |      0.8      |       200       |      0.8       |     uniform     |    average     |        0.8        |      uniform      |     0.01      |      2000       |  0.0001   | 0.5  |    400     | sorted_selection_part | Baseline  |
| 52647 |      2000       |      0.8      |       200       |      0.8       |    gaussian     |    average     |        0.8        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.8  |    400     | sorted_selection_part | Baseline  |
| 23106 |      2000       |      0.2      |       200       |      0.8       |    gaussian     |    average     |        0.2        |      uniform      |     0.01      |      2000       |  0.0001   | 0.5  |    400     | sorted_selection_all  | Baseline  |
| 23994 |      2000       |      0.2      |       200       |      0.8       |    gaussian     |    average     |        0.8        |     gaussian      |      0.1      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_all  | Baseline  |
| 8994  |      2000       |      0.2      |       200       |      0.2       |    gaussian     |    average     |        0.2        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_all  | Baseline  |
| 51930 |      2000       |      0.8      |       200       |      0.8       |    gaussian     |    average     |        0.2        |      uniform      |     0.01      |      2000       |  0.0001   | 0.8  |    400     | sorted_selection_all  | Baseline  |
| 8991  |      2000       |      0.2      |       200       |      0.2       |    gaussian     |    average     |        0.2        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 19071 |      2000       |      0.2      |       200       |      0.8       |     uniform     |    average     |        0.8        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_part | Baseline  |
| 9354  |      2000       |      0.2      |       200       |      0.2       |    gaussian     |    average     |        0.8        |      uniform      |      0.1      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_all  | Baseline  |
| 52119 |      2000       |      0.8      |       200       |      0.8       |    gaussian     |    average     |        0.2        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.2  |    400     | sorted_selection_part | Baseline  |
| 56994 |      2000       |      0.8      |       200       |      0.8       | frequency_based |    average     |        0.2        |     gaussian      |     0.01      |      2000       |  0.0001   | 0.99 |    400     | sorted_selection_all  | Baseline  |