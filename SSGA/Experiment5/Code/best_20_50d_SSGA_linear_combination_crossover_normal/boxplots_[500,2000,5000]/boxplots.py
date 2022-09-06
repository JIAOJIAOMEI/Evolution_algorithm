# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/18/22 07:08
import numpy as np
import pandas as pd
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "combination_216.csv",
    index_col=[0, 1],
    header=0,
)
# display(df)
com_df = pd.read_csv(
    "combinations_result_baseline.csv",
    header=0,
)
# display(com_df)

df.columns = [i for i in range(1, len(com_df) + 1, 1)]
df = df.stack()
df = df.rename_axis(index=["Function", "Times", "Combinations"])
df = df.reset_index(level=[0, 2], name="Fitness")
df = df.reset_index(drop=False)
# display(df.columns)

df[['iterations', 'mutation_rate', 'local_search', 'num_individuals',
    'm_range', 'range_mutation', 'crossover_probability']] = pd.DataFrame(
    [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], index=df.index)

for i in range(0, len(com_df), 1):
    # print(i)
    df.loc[df['Combinations'] == i + 1, 'iterations'] = com_df.iloc[i, 0]
    df.loc[df['Combinations'] == i + 1, 'mutation_rate'] = com_df.iloc[i, 1]
    df.loc[df['Combinations'] == i + 1, 'num_individuals'] = com_df.iloc[i, 2]
    df.loc[df['Combinations'] == i + 1, 'range_mutation'] = com_df.iloc[i, 3]
    df.loc[df['Combinations'] == i + 1, 'crossover_probability'] = com_df.iloc[i, 4]

df["Fitness"] = df["Fitness"].astype("float64")
# print(df)
df.to_csv("./plot_df.csv.csv",
          header=True,
          index=True)

df = pd.read_csv("plot_df.csv",
                 header=[0],
                 index_col=0)
display(df)


def show_graph(df, lst, f):
    sns.set()
    dist_cols = 2
    dist_rows = 2
    plt.figure(figsize=(12 * dist_cols, 12 * dist_rows))
    i = 1
    for k in range(len(lst)):
        ax = plt.subplot(dist_rows, dist_cols, i)
        # ax = sns.violinplot(x=lst[k], y="Fitness",hue="Type",data=df,ax=ax, margin_titles=True, palette="Set2",legend=True, dodge=True, inner="quartile")
        ax = sns.barplot(x=lst[k], y="Fitness", hue="iterations", data=df, palette="Set2")
        ax.set_ylabel("Fitness value")
        ax.set_xlabel("parameter range")
        ax.set_title(lst[k])
        i = i + 1
    plt.savefig('barplot_F{0}.pdf'.format(f), dpi=1000)
    plt.show()


cols = ['mutation_rate', 'num_individuals', "range_mutation", 'crossover_probability']

for i in np.arange(1,24,1):
    cond = df["Function"] == "F" + str(i)
    show_graph(df=df[cond], lst=cols, f=i)
