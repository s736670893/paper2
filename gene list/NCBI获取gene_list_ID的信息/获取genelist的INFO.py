import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def get_info(gene_id):
    url = "https://www.ncbi.nlm.nih.gov/gene/?term="+str(gene_id)
    response = requests.get(url)
    flag = 0
    while response.status_code != 200 and flag < 100:
        response = requests.get(url)
        flag += 1
    try:
        soup = bs(response.text, "html.parser")
        target = soup.find(id="summaryDl")
        res = target.find_all(re.compile("[dt|dd]"))
        for i in range(len(res)):
            if res[i].text == "Gene type":
                return [gene_id, res[i+1].text]
    except:
        print(url)


if __name__ == "__main__":
    gene_list = pd.read_table("2018_gene_list_gene_ID.txt", header=None)
    result = []
    count = 0
    # with open("2018_gene_list_gene_ID_with_INFO.txt", "w") as fw:
    #     for gene_id in gene_list[0].values:
    #         res = get_info(gene_id)
    #         fw.write(str(res[0])+"\t"+res[1]+"\n")
    #         print("第{}次".format(count))
    #         print(res[0], "  ", res[1])
    #         count += 1
    for gene_id in gene_list[0].values:
        fw = open("2018_gene_list_gene_ID_with_INFO.txt", "a")
        res = get_info(gene_id)
        fw.write(str(res[0])+"\t"+res[1]+"\n")
        fw.close()
        print("第{}次".format(count))
        print(res[0], "  ", res[1])
        count += 1

