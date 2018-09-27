## 每个文件注释
    2018_gene_list_gene_ID.txt：去重以后的gene ID
    2018_gene_list_gene_ID.xlsx：去重以后的gene ID
    获取genelist的INFO.py：使用爬虫根据2018_gene_list_gene_ID.txt获取相应的INFO
    2018_gene_list_gene_ID_with_INFO.txt：获取最终gene_id对应的INFO
    
    gene_id_to_gene_name.txt：记录gene_id和gene_name映射关系
    get_gene_name_by_id.py：根据2018_gene_list_gene_ID_with_INFO.txt中gene_id获取gene_name.
    存入2018_gene_list_gene_ID_with_INFO_01.txt,然后转换为result_gene_list.xlsx文件
