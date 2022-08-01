# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
import matplotlib.pyplot as plt
import pandas as pd
from IPython.core.display_functions import display

Baldwin = pd.read_csv(
    "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/Short_format_table/Baldwin_table_short_four_1_3072.csv",
    index_col=[0, 1],
    header=0,
    sep=","
)
Baldwin.columns = [i for i in range(1, 3073, 1)]
display(Baldwin)

df = Baldwin


def show(i):
    x = df.columns
    y1 = df.loc[i].loc["Mean"]
    y2 = df.loc[i].loc["Max"]
    y3 = df.loc[i].loc["Min"]
    plt.figure(figsize=(60, 10), dpi=1000)
    plt.scatter(x, y1, color='lawngreen', marker='*')
    plt.scatter(x, y2, color="cyan", marker='*')
    plt.scatter(x, y3, color='magenta', marker='*')  # 线宽、透明度
    plt.legend(['Mean', "Max", "Min"], fontsize=40, loc='center', ncol=3, bbox_to_anchor=[0, 1.05, 1, 0.2])
    plt.tight_layout()
    plt.savefig('./{0}.pdf'.format(i),
                dpi=1000,
                bbox_inches='tight')


k = ["F" + str(i) for i in range(1, 24, 1)]
for i in k:
    show(i)
