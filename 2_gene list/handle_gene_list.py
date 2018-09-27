import pandas as pd
from functools import reduce


def extended(a, b):
    a.extend(b)
    return a

if __name__ == "__main__":
    d1 = pd.read_csv(open("2018_gene_list.csv")).values.tolist()
    d2 = pd.read_csv(open("2018_gene_list(去重).csv")).values.tolist()

    d1 = reduce(lambda x, y: extended(x, y), d1)
    d2 = reduce(lambda x, y: extended(x, y), d2)

    s1 = list(set(d1))

    s1_sub_d2 = [x for x in s1 if x not in d2] + [x for x in d2 if x not in s1]

    pass
