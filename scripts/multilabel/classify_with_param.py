import MeCab
import sys
import os
import pdb # pdb.set_trace() でpry的なことができる。
import pandas as pd

from sklearn.externals import joblib

def tokenize(text):
    tokens = []
    m = MeCab.Tagger()
    m.parse('')
    docs = m.parseToNode(text)
    while docs :
      if docs.feature.split(",")[0] == "名詞" :
          tokens.append(docs.surface)
      docs = docs.next

    return tokens

def main():
    # 学習モデルロード
    clf = joblib.load(os.path.dirname(os.path.abspath(__file__)) + '/learn_data/clf.pkl')

    # 分類したいデータのロード
    args = sys.argv
    print('第１引数：' + args[1])
    data = [args[1]]

    # delimiter = "\n"
    # with open('./train_data/hoge.txt', "rU") as f:
    #     data = [v.rstrip() for v in f.readlines()]

    # タグのリストを取得
    data_df = pd.read_csv("./train_data/train_data.tsv", delimiter='\t')
    genres = list(data_df.drop(['id', 'title', 'content'], axis=1).columns.values)

    # 出力
    print("Applying best classifier on test data:")
    predictions = clf.best_estimator_.predict(data)

    tag_list = []
    for predict in predictions :
        for index, value in enumerate(predict):
            if value == 1 :
                tag_list.append(genres[index])

    print(tag_list)

if __name__ == "__main__":
    main()
