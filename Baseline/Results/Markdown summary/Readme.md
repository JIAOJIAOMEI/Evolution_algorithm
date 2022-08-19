# version 2

for this baseline function, there are 6 combinations of different mutation_types and crossover_types:

1. "Linear_combination_crossover_normal" 
2. "Linear_combination_crossover_uniform"
3. "Probabilistic_crossover_normal"
4. "Probabilistic_crossover_uniform"
5. "singe_point_crossover_normal"
6. "singe_point_crossover_uniform"

```
Sequence for iterations : [1000000]
Sequence for mutation_rate : [0.1, 0.18, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
Sequence for num_individuals : [100, 200]
Sequence for range_mutation : [0.01, 0.25, 0.55, 0.9, 2.0, 5.0]
Sequence for crossover_probability : [0.5, 0.6, 0.7]
```

==for the bar-plots:==

- One million iterations, there is nothing to analyze about this.

- For the mutation rate parameter, as the value of mutation rate rises, f1 f3 f6 12 and f18 have a tendency to fall first and then rise, basically reaching a minimum at about 0.5 and then start to rise. So I think the best value for the mutation rate is not to exceed 0.5.
- For the parameter num_individuals, since there are only 100 and 200, but basically it is observed that the performance of 200 is much better than 100, showing a decreasing trend.
- For the mutation range parameter, most of the functions still show a decreasing and then increasing trend, with the inflection point at 0.9.
- Finally, the crossover probabilities are all downward trending.

barplots each picture I have marked, you can take a look.

==for data_analyis plots:==

The data analysis diagram is differentiated according to each parameter combination, with the horizontal coordinate representing the actual calculated solution and the vertical coordinate representing the number.

In general, the performance of singe_point_crossover_uniform is very bad, and there is a big gap between it and the other ones.

However, given the combinations 111,129,145, 146, 147, 163, 164, 165, 181, 182, 183, 199 and 200, even the poor performing singe_point_crossover_uniform can find the minimum value.
There are other parameters that perform well, but not as significantly.

I think this information is useful.

==for percent csv==:

generally speaking,

1. regarding mutation_type, normal distribution is obviously better than uniform distribution.
2. regarding crossover_type. Linear_combination_crossover > Probabilistic_crossover > singe_point_crossover

# version 1

**six functions**: f1 f3 f6 f12 f18 f22

**Dimensions**: 50 dimensinal functions are downgraded to 10

**Combiantions**: only the first 100 are generated. See "combinations_result_baseline.txt"

```
Sequence for iterations : [1000000]
Sequence for mutation_rate : [0.1, 0.18, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
Sequence for num_individuals : [100, 200]
Sequence for range_mutation : [0.01, 0.25, 0.55, 0.9, 2.0, 5.0]
Sequence for crossover_probability : [0.5, 0.6, 0.7]
```

Optimal solution :

```
opt = [0, 0, 0, 0, 0, 0, 0, -418.98 * 10, 0, 0, 0, 0, 0, 1, 0.00030, -1.0316, 0.398, 3, -3.86, -3.32, -10.1532, -10.4028, -10.5363]
```

**Percentage_table**:

for this baseline function, there are 6 combinations of different mutation_types and crossover_types:

1. "Linear_combination_crossover_normal" 
2. "Linear_combination_crossover_uniform"
3. "Probabilistic_crossover_normal"
4. "Probabilistic_crossover_uniform"
5. "singe_point_crossover_normal"
6. "singe_point_crossover_uniform"

**for each function and each parameter combination, "data_analysis.pdf" compares the performances of different types.**

**for each function and each parameter combination, "percentage.pdf" compares the num of optimal values of different types.**

- True means it finds the optimal solution
- False means not.

each parameter combiantion, **10** runs.

## conclusion

generally speaking,

1. regarding mutation_type, normal distribution is obviously better than uniform distribution.
2. regarding crossover_type. Linear_combination_crossover > Probabilistic_crossover > singe_point_crossover
3. for the 6 functions, 
   f1 f3 f6 and f18 can find the optimal solution in most cases.
   f22 does not perfrom very well, the percentage is like 40%.
   I think f12 has some errors because some values appear to be smaller than zero which is supposed to be to optimal. I will chekc it again and find the reason.and for function 18, as i remember, two solutions are lower than the optimal, I don't understand see data_analysis_f18.pdf .The rest combinations are still running.
4. About the barplot, I still need to think about it.



```
1000000,0.1,100,0.01,0.5,
1000000,0.1,100,0.01,0.6,
1000000,0.1,100,0.01,0.7,
1000000,0.1,100,0.25,0.5,
1000000,0.1,100,0.25,0.6,
1000000,0.1,100,0.25,0.7,
1000000,0.1,100,0.55,0.5,
1000000,0.1,100,0.55,0.6,
1000000,0.1,100,0.55,0.7,
1000000,0.1,100,0.9,0.5,
1000000,0.1,100,0.9,0.6,
1000000,0.1,100,0.9,0.7,
1000000,0.1,100,2.0,0.5,
1000000,0.1,100,2.0,0.6,
1000000,0.1,100,2.0,0.7,
1000000,0.1,100,5.0,0.5,
1000000,0.1,100,5.0,0.6,
1000000,0.1,100,5.0,0.7,
1000000,0.1,200,0.01,0.5,
1000000,0.1,200,0.01,0.6,
1000000,0.1,200,0.01,0.7,
1000000,0.1,200,0.25,0.5,
1000000,0.1,200,0.25,0.6,
1000000,0.1,200,0.25,0.7,
1000000,0.1,200,0.55,0.5,
1000000,0.1,200,0.55,0.6,
1000000,0.1,200,0.55,0.7,
1000000,0.1,200,0.9,0.5,
1000000,0.1,200,0.9,0.6,
1000000,0.1,200,0.9,0.7,
1000000,0.1,200,2.0,0.5,
1000000,0.1,200,2.0,0.6,
1000000,0.1,200,2.0,0.7,
1000000,0.1,200,5.0,0.5,
1000000,0.1,200,5.0,0.6,
1000000,0.1,200,5.0,0.7,
1000000,0.18,100,0.01,0.5,
1000000,0.18,100,0.01,0.6,
1000000,0.18,100,0.01,0.7,
1000000,0.18,100,0.25,0.5,
1000000,0.18,100,0.25,0.6,
1000000,0.18,100,0.25,0.7,
1000000,0.18,100,0.55,0.5,
1000000,0.18,100,0.55,0.6,
1000000,0.18,100,0.55,0.7,
1000000,0.18,100,0.9,0.5,
1000000,0.18,100,0.9,0.6,
1000000,0.18,100,0.9,0.7,
1000000,0.18,100,2.0,0.5,
1000000,0.18,100,2.0,0.6,
1000000,0.18,100,2.0,0.7,
1000000,0.18,100,5.0,0.5,
1000000,0.18,100,5.0,0.6,
1000000,0.18,100,5.0,0.7,
1000000,0.18,200,0.01,0.5,
1000000,0.18,200,0.01,0.6,
1000000,0.18,200,0.01,0.7,
1000000,0.18,200,0.25,0.5,
1000000,0.18,200,0.25,0.6,
1000000,0.18,200,0.25,0.7,
1000000,0.18,200,0.55,0.5,
1000000,0.18,200,0.55,0.6,
1000000,0.18,200,0.55,0.7,
1000000,0.18,200,0.9,0.5,
1000000,0.18,200,0.9,0.6,
1000000,0.18,200,0.9,0.7,
1000000,0.18,200,2.0,0.5,
1000000,0.18,200,2.0,0.6,
1000000,0.18,200,2.0,0.7,
1000000,0.18,200,5.0,0.5,
1000000,0.18,200,5.0,0.6,
1000000,0.18,200,5.0,0.7,
1000000,0.2,100,0.01,0.5,
1000000,0.2,100,0.01,0.6,
1000000,0.2,100,0.01,0.7,
1000000,0.2,100,0.25,0.5,
1000000,0.2,100,0.25,0.6,
1000000,0.2,100,0.25,0.7,
1000000,0.2,100,0.55,0.5,
1000000,0.2,100,0.55,0.6,
1000000,0.2,100,0.55,0.7,
1000000,0.2,100,0.9,0.5,
1000000,0.2,100,0.9,0.6,
1000000,0.2,100,0.9,0.7,
1000000,0.2,100,2.0,0.5,
1000000,0.2,100,2.0,0.6,
1000000,0.2,100,2.0,0.7,
1000000,0.2,100,5.0,0.5,
1000000,0.2,100,5.0,0.6,
1000000,0.2,100,5.0,0.7,
1000000,0.2,200,0.01,0.5,
1000000,0.2,200,0.01,0.6,
1000000,0.2,200,0.01,0.7,
1000000,0.2,200,0.25,0.5,
1000000,0.2,200,0.25,0.6,
1000000,0.2,200,0.25,0.7,
1000000,0.2,200,0.55,0.5,
1000000,0.2,200,0.55,0.6,
1000000,0.2,200,0.55,0.7,
1000000,0.2,200,0.9,0.5,
1000000,0.2,200,0.9,0.6,
1000000,0.2,200,0.9,0.7,
1000000,0.2,200,2.0,0.5,
1000000,0.2,200,2.0,0.6,
1000000,0.2,200,2.0,0.7,
1000000,0.2,200,5.0,0.5,
1000000,0.2,200,5.0,0.6,
1000000,0.2,200,5.0,0.7,
1000000,0.5,100,0.01,0.5,
1000000,0.5,100,0.01,0.6,
1000000,0.5,100,0.01,0.7,
1000000,0.5,100,0.25,0.5,
1000000,0.5,100,0.25,0.6,
1000000,0.5,100,0.25,0.7,
1000000,0.5,100,0.55,0.5,
1000000,0.5,100,0.55,0.6,
1000000,0.5,100,0.55,0.7,
1000000,0.5,100,0.9,0.5,
1000000,0.5,100,0.9,0.6,
1000000,0.5,100,0.9,0.7,
1000000,0.5,100,2.0,0.5,
1000000,0.5,100,2.0,0.6,
1000000,0.5,100,2.0,0.7,
1000000,0.5,100,5.0,0.5,
1000000,0.5,100,5.0,0.6,
1000000,0.5,100,5.0,0.7,
1000000,0.5,200,0.01,0.5,
1000000,0.5,200,0.01,0.6,
1000000,0.5,200,0.01,0.7,
1000000,0.5,200,0.25,0.5,
1000000,0.5,200,0.25,0.6,
1000000,0.5,200,0.25,0.7,
1000000,0.5,200,0.55,0.5,
1000000,0.5,200,0.55,0.6,
1000000,0.5,200,0.55,0.7,
1000000,0.5,200,0.9,0.5,
1000000,0.5,200,0.9,0.6,
1000000,0.5,200,0.9,0.7,
1000000,0.5,200,2.0,0.5,
1000000,0.5,200,2.0,0.6,
1000000,0.5,200,2.0,0.7,
1000000,0.5,200,5.0,0.5,
1000000,0.5,200,5.0,0.6,
1000000,0.5,200,5.0,0.7,
1000000,1.0,100,0.01,0.5,
1000000,1.0,100,0.01,0.6,
1000000,1.0,100,0.01,0.7,
1000000,1.0,100,0.25,0.5,
1000000,1.0,100,0.25,0.6,
1000000,1.0,100,0.25,0.7,
1000000,1.0,100,0.55,0.5,
1000000,1.0,100,0.55,0.6,
1000000,1.0,100,0.55,0.7,
1000000,1.0,100,0.9,0.5,
1000000,1.0,100,0.9,0.6,
1000000,1.0,100,0.9,0.7,
1000000,1.0,100,2.0,0.5,
1000000,1.0,100,2.0,0.6,
1000000,1.0,100,2.0,0.7,
1000000,1.0,100,5.0,0.5,
1000000,1.0,100,5.0,0.6,
1000000,1.0,100,5.0,0.7,
1000000,1.0,200,0.01,0.5,
1000000,1.0,200,0.01,0.6,
1000000,1.0,200,0.01,0.7,
1000000,1.0,200,0.25,0.5,
1000000,1.0,200,0.25,0.6,
1000000,1.0,200,0.25,0.7,
1000000,1.0,200,0.55,0.5,
1000000,1.0,200,0.55,0.6,
1000000,1.0,200,0.55,0.7,
1000000,1.0,200,0.9,0.5,
1000000,1.0,200,0.9,0.6,
1000000,1.0,200,0.9,0.7,
1000000,1.0,200,2.0,0.5,
1000000,1.0,200,2.0,0.6,
1000000,1.0,200,2.0,0.7,
1000000,1.0,200,5.0,0.5,
1000000,1.0,200,5.0,0.6,
1000000,1.0,200,5.0,0.7,
1000000,2.0,100,0.01,0.5,
1000000,2.0,100,0.01,0.6,
1000000,2.0,100,0.01,0.7,
1000000,2.0,100,0.25,0.5,
1000000,2.0,100,0.25,0.6,
1000000,2.0,100,0.25,0.7,
1000000,2.0,100,0.55,0.5,
1000000,2.0,100,0.55,0.6,
1000000,2.0,100,0.55,0.7,
1000000,2.0,100,0.9,0.5,
1000000,2.0,100,0.9,0.6,
1000000,2.0,100,0.9,0.7,
1000000,2.0,100,2.0,0.5,
1000000,2.0,100,2.0,0.6,
1000000,2.0,100,2.0,0.7,
1000000,2.0,100,5.0,0.5,
1000000,2.0,100,5.0,0.6,
1000000,2.0,100,5.0,0.7,
1000000,2.0,200,0.01,0.5,
1000000,2.0,200,0.01,0.6,
```

