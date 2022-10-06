
$$
Score_{k}^{F} = \sum_{j=1}^{6}\sum_{i=1}^{10} (Solution_{i}^{J}-F_{*})
$$
where $F$ represents a function, $F_{*}$ represents the global minima for this function, $F$ can be {$F1$,$F3$,$F6$,$F12$,$F18$,$F22$}
$J$ means a combination of crossover type and mutation type, $J$ can be {1: (N,Pc), 2: (N,SPc), 3:(N,LCc), 4: (U,Pc), 5:(U,SPc), 6:(U,LCc)},
$Solution_{i}^{J}$ means  $i$th times solution calculated by a parameter combination given $J$, 
$k$ is the index of a parameter combination, $k$ can be [1,2,3,...,200],
$Score_{k}^{F}$ represents the score for a parameter combination given function $F$.

$Score^{F}$ is a list which contains all the scores of 200 parameter combinations given function $F$.

The process for selecting best 20 parameter combinations:

1. For $F1$,$F3$,$F6$,$F12$,$F18$ and $F22$, calculate $Score^{F1}$, $Score^{F3}$, $Score^{F6}$, $Score^{F12}$, $Score^{F18}$ and $Score^{F22}$ separately
2. Rank $Score^{F1}$, $Score^{F3}$, $Score^{F6}$, $Score^{F12}$, $Score^{F18}$ and $Score^{F22}$ in an ascending order separately;
3. Choose the first 20 scores in each sorted list and find the corresponding parameter combinations according to the index of each score; 
4. Merge best 20 parameter combinations of $F1$,$F3$,$F6$,$F12$,$F18$ and $F22$;
5. Count the number of times that each parameter combination appears;
6. Based on the frequency counted in step 4, choose most frequent 20 parameter combinations as final decision.