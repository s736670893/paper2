import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def get_gene_list(gene_id):
    url = "http://dbemt.bioinfo-minzhao.org/literature_highlight.cgi?gene="+str(gene_id)
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    target = soup.find_all("td", class_="content")
    text = target[7].text
    text = text.replace("\t", "").replace("\n", "")
    with open("gene_abstract.txt", "a") as fw:
        fw.write(str(gene_id)+"\t"+text+"\n")


if __name__ == "__main__":
    data = pd.read_csv(open("EMT_数据库.csv"), header=None)
    gene_id = data.iloc[:, 0].values
    for id in gene_id:
        gene = get_gene_list(id)
