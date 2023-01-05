# description of the whole algorithm

The process of whole algorithm is:

1. create a population
2. selection
3. crossover (two parents--------->one child)
4. mutation (one child-------->one mutation result)
5. local search (one mutation result: genotype------->one phenotype)
6. update the population and repeat step 2~6

## selection operators

4 selection operators are implemented:

In each selection operator, the population is divided into 3 groups: the first group is "eligible individuals", the second group is "eligible partners", the third group is "non eligible individuals".

1. **best and worst**: "eligible individuals" only contain the best individual who has the lowest fitness value in the entire population, "non eligible individuals" only contain the worst individual who has the highest fitness value, and "eligible partners" contain the whole population except for "non eligible individuals". 
2. **sorted_selection_part**: "eligible individuals" contain the best **N** individuals who has the lowest fitness value in the entire population, wherein *N=number of individuals times generation gap*, "non eligible individuals" contain the worst **N** individuals who has the highest fitness value, and "eligible partners" contain the whole population except for "non eligible individuals".  **If "generation gap" is 0.01 or 0.99, then at least one individual is selected.**
3. **sorted_selection_all**: "eligible individuals" contain the best **N** individuals who has the lowest fitness value in the entire population, wherein *N=number of individuals times generation gap*, "non eligible individuals" contain the worst **N** individuals who has the highest fitness value, **and "eligible partners" contain the whole population**.
4. **roulette_Wheel_Select**: "non eligible individuals" contain **N** individuals, which are selected based on their probabilities. The higher the fitness value, the higher the probability to be selected. *Probability= abs(fitness value)/ sum of abs(fitness values) for the entire population*. "eligible individuals" also contain **N** individuals, which are selected based on the inverse probabilities. *Inverse probablity = 1-probability*.The lower the fitness value, the higher the probability to be selected, and "eligible partners" contain the whole population except for "non eligible individuals". 

## crossover operators

For each eligible individual in "eligible individuals", a partner is randomly matched in "eligible partners". This is how I get the two parents for crossover.("Baseline" or "Baldwin": genotype, "Lamarck": phenotype).

parent1 in an eligible individual, and parent2 is the partner.

1. **one point**: if a random probability is more than "crossover rate", then randomly pick a parent as the result. Otherwise, choose a random crossover point and exchange two parents' tails, then two children are born, and randomly pick one to do later operators. 
2. **two point**: if a random probability is more than "crossover rate", then randomly pick a parent as the result. Otherwise, choose two random crossover points and exchange the middle parts of the parents, then randomly choose one child as the result.  
3. **probabilistic crossover**: for each gene, if a random probability is less than "crossover rate", then the child gets the gene from parent1, otherwise he gets the gene from parent2.
4. **linear_combination_crossover**: for each gene, *child= "crossover rate" times parent1+(1-"crossover rate") times parent2*.
5. **average**: for each gene, *child = (parent1+parent2) times (1-"crossover rate") /2*.
6. **roulette_wheel_crossover**: for parent1, calculate the probability for each gene based on the fitness value. *prob1 = abs(fitness)/sum of abs(fitness) of parent1*.  get the same thing *prob2* for parent2. Then if *prob1* or *prob2* is more than "crossover rate", then child will get the minimum gene of parent1 and parent2, otherwise the child will get a new gene between gene of parent1 and gene of parent2.

## mutation operators

after get the one child of crossover, then begin the mutation.

3 mutation operators are implemented:

1. **uniform**: each gene must fall into the domain of a function. The domian of the function is "genotype_range", it contains a lower value and a higher value, an interval. "search radius" controls the range for mutation. *"mutation_range" =["search radius" times lower value, "search radius" time higher value]*.  For each gene, if a random probability is less than "mutation rate", then plus a uniformly sampled variable in "mutation range".
2. **guassian**: same as above, just the variable is sampled from a gussian distribution. *mean=0, std = "mutation_range"/6*
3. **frequency_based_mutation**: the domian is divdied equally into 10 categories. Count the number of the genes falling into each category. *probability of each category=number of genes in one catergory/ number of genes*. The probability for each gene is depending on which category it falls in. *probability of each gene = 1- probability of its catergory*. For each gene, if the probability is more than "mutation rate", then plus a uniformly sampled variable within the "mutation_range".

The range of each gene is checked and all of them falls into the domain of the function.

## local search operators

1. **uniform**: the range for local seach is the same as the range for mutation. For each gene in the genotype, if a random probability is less than "local search rate", then plus a uniformly sampled variable in "local search range", otherwise $phenotype_{i}=genotype{i}$.
2. **guassian**: same as above, just the variable is sampled from a gussian distribution. *mean=0, std = "local seach range"/6*
3. **neighbor search**: if a random probability is less than "local search rate", then $phenotype_{i} = min(abs(genotype_{i-1}),abs(genotype_{i}),abs(genotype_{i+1}))$, otherwise $phenotype_{i}=abs(genotype{i})$.

# parameters of the algorithms

16 parameters in total.

1. **num_generations**: the max number of iteratiosn
2. **mutation_rate**: a float number between 0 and 1
3. **num_individuals**: number of the whole population
4. **crossover_rate**: a float number between 0 and 1
5. **mutation_type**: 4 mutation operators
6. **crossover_type**: 6 crossover operators
7. **local_search_rate**: a float number between 0 and 1
8. **local_search_type**: 3 local search operators
9. **search_radius**: it controls the range for mutation and local seach, a float number between 0 and 1
10. **num_evaluations**: the max number of using f.()
11. **fitness_function**: 23 fitness functions
12. **dimensions**: a positive integer, it can change dimensions of 13/23 functions because 13 funcitons' diemension is flexible, not fixed.
13. **algorithm**: 3 algorithms, "Baseline","Baldwin" and "Lamarck"
14. **gg**: generation gap, a float number between 0 and 1
15. **selection_method**: 4 selection operators
16. **num_runs**: it is the number of runs for each parameter combination(first 15 parameter combinations).

That's all for this experiment.

## stopping condition

If **num_generations** or **num_evaluations** is reached, then stop. No one knows the global minimum.

# values that might be run

1. **num_generations**: [1000]
2. **mutation_rate**: [0.2 , 0.8]
3. **num_individuals**: [500]
4. **crossover_rate**: [0.2 , 0.8]
5. **mutation_type**: 4 mutation operators
6. **crossover_type**: 6 crossover operators
7. **local_search_rate**: [0.2 , 0.8]
8. **local_search_type**: 3 local search operators
9. **search_radius**: [0.05, 0.1]
10. **num_evaluations**: [10000]
11. **fitness_function**: [1,8,12,15,20,21]
12. **dimensions**: [100, 400]
13. **algorithm**: 3 algorithms, "Baseline","Baldwin" and "Lamarck"
14. **gg**: [0.01,0.2,0.8,0.99]
15. **selection_method**: 4 selection operators
16. **num_runs**: [10]



