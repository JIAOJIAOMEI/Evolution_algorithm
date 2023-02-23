# Feedback about Experiment15

1) **PROBLEM_1: Local search (individual learning) does not bring as much benefit as it costs in budget.** 

In the real, biological world, an individual that is learning during its lifetime is always better off than one that cannot change its behavior. (Even if what is learned by the individual is not passed on to the next generation.) It is very hard to argue with this. Yet, in our abstract setting, PROBLEM_1 exists, which essentially means that the costs of this individual learning is too much: **the costs of learning are higher than the benefits of it**. Our (biologically motivated) observation is that one major difference between 'real life' and our abstract setting is that in real life learning can occur, because the individual is facing the same (or very similar) decision making problems during its life. For example, it needs to hunt every day. So, if it gets better and better in it, it is useful, compared to the case when it just performs the same (inherited) method over and over again. The key difference here from our abstract setting is that the 'action' needs to be evaluated repeatedly in any case (**hunting is 'evaluated' each day**), independent of the fact that there is learning or not. So, if the problem is such that you need to evaluate the 'fitness function' several times for an individual, no matter what, then learning is not an extra cost...

One way to model this in our abstract setting is to ==calculate the fitness of an individual as F(genotype) + F(phenotype)==. In case of SSGA phenotype=genotype, so it will get less information for the same budget.

This is a direct model of the above, biologically described situation. But it is not overly 'elegant' as it doctors the original problem (and makes it directly favourable to memetic approaches). In principle, we could find problem domains (and should be able to do it successfully), where such iterative actions exist by default.

2) **PROBLEM_2: Local search is not effective in getting out from local minima valleys.** 

Here we have an idea to change/improve the way local search is performed. (Actually, this has been proposed before in the literature in a different context, but could be very useful here.) The idea is to invest some more budget in the local search, in the hope to get better results out of it. The nice thing is that it is a true generalisation of our current approach. Therefore, the current approach is a special case of this proposal. Let's call it, iterative local search.

**Algorithm:**

```
p0 = genotype
i=0
while (i<length_of_local_search):   # This is a new parameter. Determines the length of the iteration
  p1 = LS(p0) # This performs our current local search procedure on the genotype. 
              # I.e., if makes a random sample in the vicinity of the genotype, according to the many parameters we have.
  if p0<p1:  
   p1 = p0  
   p0 = p1
i = i + 1

phenotype = p1
```

So, basically, we do the sampling iteratively. (Note, that an alternative version would be to move the "if p0<p1: p1=p0" part to the end, outside of the loop. (That way, we would give more support to coming out of a valley by allowing intermediate steps that would be worse than the current best.)  -- We could possibly do both. 

3) **PROBLEM_3: The population is too similar (converges quickly).**

Here the idea to address this problem is to make local search more widely applied. Again, this also means that we invest more budget in local search, but the hope is that it will bring higher benefits, so that will compensate for this.

**The key observation that drives this idea is that in the current version, local search is only applied to the best individual.** All the rest of the population is 'passive' -- and thus gets eventually (actually, very quickly similar) to the best one. To compensate it, we propose to do local search, in each round, not only for the new offspring, but generally, for a certain fraction (a new parameter, say, **f%**) of the entire population. So, once the new offspring is created, then we make a sample of the new popoulation (f% of it) and do our normal local search (see below) for them. This way, individuals who are not the best also have a chance to improve and also to diversify themselves from the current best:

```
p0 = genotype
p1 = LS(p0)
if p0<p1:
 p1 = p0
phenotype = p1
```

