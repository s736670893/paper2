import pandas as pd


if __name__ == "__main__":
    gene_id_to_name = pd.read_table("gene_id_to_gene_name.txt", sep="\t").values
    dic = dict()
    for tmp in gene_id_to_name:
        if tmp[0] not in dic.keys():
            dic[tmp[0]] = tmp[1]

    fw = open("2018_gene_list_gene_ID_with_INFO_01.txt", "w")
    with open("2018_gene_list_gene_ID_with_INFO.txt", "r") as fr:
        for line in fr.readlines():
            a, b = line.split("\t")
            fw.write(a+"\t"+dic[int(a)]+"\t"+b)
    fw.close()
    pass

