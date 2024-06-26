# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 7/30/22 15:35
import pandas as pd


def combination():
    com = []
    iterations = [100]
    mutation_rate = [5.0, 10.0]
    local_search = [0.01, 1.0, 5.0]
    num_individuals = [50, 400, 800]
    m_range = [0.05, 0.35, 0.8, 1.2]
    range_mutation = [0.01, 0.25, 0.55, 0.9]
    crossover_probability = [0.4, 1.0]
    num_phenotypes = [3]
    for a in iterations:
        for b in mutation_rate:
            for c in local_search:
                for d in num_individuals:
                    for e in m_range:
                        for f in range_mutation:
                            for g in crossover_probability:
                                for h in num_phenotypes:
                                    G = [a, b, c, d, e, f, g, h]
                                    com.append(G)
    sequence_list = [str(iterations), str(mutation_rate), str(local_search), str(num_individuals), str(m_range),
                     str(range_mutation), str(crossover_probability), str(num_phenotypes)]
    name = ["iterations", "mutation_rate", "local_search", "num_individuals", "m_range", "range_mutation",
            "crossover_probability", "num_phenotypes"]

    with open("combinations_result.txt", 'w+', encoding='utf-8') as f:
        for x, sequence in zip(name, sequence_list):
            f.writelines("Sequence for {0} : {1}".format(x, sequence))
            f.write("\n")
        for i in range(len(com)):
            for j in range(len((com[i]))):
                f.write(str(com[i][j]))
                f.write(",")
            f.write("\n")

    df = pd.DataFrame(data=com, index=["Combination" + str(i + 1) for i in range(len(com))],
                      columns=["iterations", "mutation_rate", "local_search", "num_individuals", "m_range",
                               "range_mutation", "crossover_probability", "num_phenotypes"])
    df.to_csv('combinations_result.csv',
              header=True,
              index=False)


def read_com():
    com = pd.read_csv("./combinations_result.csv",
                      header=0,
                      index_col=None)
    return com


def read_file(sheetname, path):
    df = pd.read_excel(path, sheet_name=sheetname,
                       header=0,
                       index_col=[0, 1])
    df = df.rename_axis(["Function", "Times"])
    return df
