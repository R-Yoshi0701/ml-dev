#coding:utf-8

import json
import MeCab
m = MeCab.Tagger()

if __name__ == '__main__':

    article_tag_file = open('../../train_data/ferret_articletag.csv','r')
    article_file = open('../../train_data/ferret_article.tsv','r')
    train_data = open('train_data.tsv','w')

    tags = article_tag_file.readlines()
    articles = article_file.readlines()

    train_data.write("id\ttitle\tcontent")
    for tag in tags :
        train_data.write("\t" + tag.strip())
    train_data.write("\n")

    for article in articles :
        id = article.split("\t")[0]
        title = article.split("\t")[2]
        doc = article.split("\t")[4]
        docs = m.parseToNode(article.split("\t")[4])
        doc_list = []
        train_data.write(id + "\t" + title + "\t" + doc.strip())
        while docs :
          print(docs.surface)
          doc_list.append(docs.surface)
          docs = docs.next
        for tag in tags:
            i = 0
            for tag_s in tag.strip().split(","):
                if tag_s.strip() in doc_list:
                    i = 1
                    break
            train_data.write("\t" + str(i))
        train_data.write("\n")

    article_tag_file.close()
    article_file.close()
    train_data.close()
