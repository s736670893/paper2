import pandas as pd


if __name__ == "__main__":
    data = pd.read_excel("dbEMT.2018.SEP.qh.xlsx")
    check = data.Check
    gene_name = data.GeneName
    dic = dict(zip(gene_name, check))

    result_gene = pd.read_excel("result_gene_list.xlsx", header=None)

    add_col = []  # 保存在dbEMT.2018.June.qh.xlsx中存在的gene，有的在result_gene_list.xlsx中的gene，
    # 但是在dbEMT.2018.June.qh.xlsx中找不到
    extra_col = []  # 保存在result_gene_list.xlsx中，但是在dbEMT.2018.June.qh.xlsx中找不到的gene

    for i in range(result_gene.shape[0]):
        key = result_gene.iloc[i, 1]
        if key in dic.keys() and dic[key]==True:
            tmp_list = [result_gene.iloc[i, :][0], result_gene.iloc[i, :][1], result_gene.iloc[i, :][2], dic[key]]
            add_col.append(tmp_list)
        else:
            extra_col.append(key)

    add_col_df = pd.DataFrame(add_col)
    extra_col_df = pd.DataFrame(extra_col)

    add_col_df.to_excel("new_gene_list.xlsx", header=False, index=False)
    extra_col_df.to_excel("not_EMT.xlsx", header=False, index=False)

