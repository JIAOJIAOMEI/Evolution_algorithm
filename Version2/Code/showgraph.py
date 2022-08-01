# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/31/22 13:29

import pandas as pd
import numpy as np
from IPython.core.display_functions import display
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("plot_df.csv",
                 header=[0],
                 index_col=0)
display(df)


def show_graph(df, lst):
    sns.set()
    fig = plt.figure(figsize=(18, 18))
    for i in range(len(lst)):
        ax = fig.add_subplot(3, 3, i + 1)
        sns.violinplot(x=lst[i], y="Fitness", data=df,ax=ax, margin_titles=True, palette="Set2",
                       legend=True, dodge=True, inner="quartile",split=True)
        ax.set_title(lst[i])
        plt.subplots_adjust(wspace=0.3, hspace=0.3)


cols = ["iterations", 'mutation_rate', "local_search", 'num_individuals', 'm_range', "range_mutation",'crossover_probability']

for i in [1,22]:
    cond = df["Function"] == "F" + str(i)
    show_graph(df=df[cond], lst=cols)
    plt.savefig('Violin_F{0}.pdf'.format(i), dpi=1000)
