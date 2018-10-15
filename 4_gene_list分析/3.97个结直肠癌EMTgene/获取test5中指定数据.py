import pandas as pd


if __name__ == "__main__":
    d = pd.read_excel("result_test5.xlsx")
    index1 = d['adj.P.Val'] < 0.05
    index2 = abs(d['logFC']) > 0.585
    index1 = index1.tolist()
    index2 = index2.tolist()
    index = [index1[i] and index2[i] for i in range(len(index1))]
    result = d.iloc[index]
    result.to_excel("select_test5.xlsx")
