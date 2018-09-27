import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def get_gene_list():
    url = "http://dbemt.bioinfo-minzhao.org/browser.cgi"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    target = soup.find("td", class_="content")
    target2 = target.find_all("a")
    pass


if __name__ == "__main__":
    gene = get_gene_list()