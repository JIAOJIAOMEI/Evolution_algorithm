[TOC]



# Stopping conditions

3 stopping conditions in total:

- max number of iterations is reached(for this time, number of iterations is 2000.)
- max number of evaluations is reached(for this time, number of evaluations is 2000.)
- if the sum of fitnesses of phenotypes of all the population does not change in continous 20 iterations, then stop. (The threshold for defining "not change between two iterations" is 0.0001)

# performance of parameters

## Mutation rate

The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the values we tried for parameter mutation rate. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.

![mutation_rate](mutation_rate.png)

## Mutation type
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter mutation type. The y axis is the average/mean of 10 solutions produced by each parameter combination. Different color of bars represent different algorithms.


![mutation_type](mutation_type.png)

## Local seach rate
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the values we tried for parameter local search rate. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.

![local_search_rate](local_search_rate.png)

## Local search type
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter local search type. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.


![local_search_type](local_search_type.png)

## Search radius
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the values we tried for parameter search radius. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.

![search_radius](search_radius.png)

## Crossover rate
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the values we tried for parameter crossover rate. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.

![crossover_rate](crossover_rate.png)

## Crossover type
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter crossover type. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.


![crossover_type](crossover_type.png)

## Selection method
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter selection. The y axis is the average/mean of 10 solutions produced by each parameter combination.Different color of bars represent different algorithms.

![selection_method](selection_method.png)

## Generation gap:gg

![gg](gg.png)

## Conclusion
- Overall pferformance: Baseline > Lamarck > Baldwin. This conclusion seems appliciable to the both situations of dim=50 and dim=400 for now.
- The range for the final solutions produced by Baseline is wider than the other two algortihms' solutions as one can see that the boxes for Baseline are longer than the boxes for the other two. (see the plots for function=8). 

- For crossover type, the overal performance is as this: Average > Linear combination > Probabilistic > Two point $\approx$ One point. But crossover type: Average performs the worst when it comes to F8. (The average operator: $**child = (gene1 + gene2) * (1 - crossover_rate) / 2**$, the global minimum for most functions is 0, but the global minimum for F8 is dim * -498.18, I think this is why average oprator has bad effects on F8.)

- For selection method: sorted_selection_part > sorted_selection_all > SSGA $\approx$ roulette_Wheel_Select. (sorted_selection_part: the eligible partners do not include the individuals marked to be deleted; sorted_selection_all: the eligible partners include all the individuals, this means the worst genes might be passed on to the next generation.)

- For generation gap: we have tried 5 values: 0.01, 0.2, 0.5, 0.8, 0.99. The final solutions are comparable, but the range for the final solutions produced by 0.99 are much more wider than the results produced by others.

# performances of methods under different values

## Crossover rate and crossover type

The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter corssover type. The y axis is the average/mean of 10 solutions produced by each parameter combination. Different color of bars represent different algorithms. The following picture shows the performances of different crossover types under different crossover rate.

![crossover_typecombine](crossover_typecombine.png)

## Mutation rate and mutation type
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter mutation type. The y axis is the average/mean of 10 solutions produced by each parameter combination. Different color of bars represent different algorithms. The following picture shows the performances of different mutation types under different mutation rate.

![mutation_typecombine](mutation_typecombine.png)

## Local search rate and local search type
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter local search type. The y axis is the average/mean of 10 solutions produced by each parameter combination. Different color of bars represent different algorithms. The following picture shows the performances of different local search types under different local search rate.


![local_search_typecombine](local_search_typecombine.png)

## Selection method and gg
The left column is the performance plots of dimension=50, and the right column is dimension = 400. The x axis represents the methods we tried for parameter selection. The y axis is the average/mean of 10 solutions produced by each parameter combination. Different color of bars represent different algorithms. The following picture shows the performances of different selection methods under different gg.

![selection_methodcombine](selection_methodcombine.png)

## Conclusion

- For crossover type, the overal performance is as this: Average > Linear combination > Probabilistic > Two point $\approx$ One point. But crossover type: Average performs the worst when it comes to F8. (The average operator: $child = (gene1 + gene2) * (1 - crossover_{rate}) / 2$, the global minimum for most functions is **0**, but the global minimum for F8 is **dim * -498.18**, I think this is why average oprator has bad effects on F8.)
- For crossover rate, 0.8 > 0.2
- For mutation type and mutation rate, local search type and local search rate, I don't see much difference.
- For gg, 0.99>0.8>0.5>0.2>0.01
- For selection method, sorted_selection_part > sorted_selection_all > SSGA > roulette_Wheel_Select.

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

**I think these parameter combinations are chosen is because the crossover type is average. Of all the 20 parameter combinations, only crossover type has one kind of value. It souds like "No matter what the other parameter is, if you use this average crossover operator, you are going to get some good results." especially when you use average plus crossover rate = 0.8. **.

The average operator: $child = (gene1 + gene2) * (1 - crossover_{rate}) / 2$.

# Conclusion

We still have not found some good parameter combiantions where Lamarck > SSGA with the same number of evaluations.