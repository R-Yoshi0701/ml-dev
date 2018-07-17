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
    abs_path = os.path.dirname(os.path.abspath(__file__))

    # 学習モデルロード
    clf = joblib.load(abs_path + '/learn_data/clf.pkl')

    # 分類したいデータのロード
    args = sys.argv
    data = [args[1]]

    # delimiter = "\n"
    # with open(abs_path + '/train_data/hoge.txt', "rU") as f:
    #     data = [v.rstrip() for v in f.readlines()]

    # タグのリストを取得
    data_df = pd.read_csv(abs_path + "/train_data/train_data.tsv", delimiter='\t')
    genres = list(data_df.drop(['id', 'title', 'content'], axis=1).columns.values)

    # 出力
    predictions = clf.best_estimator_.predict(data)
    tag_list = []
    for predict in predictions :
        for index, value in enumerate(predict):
            if value == 1 :
                tag_list.append(genres[index])

    # result
    print(','.join(tag_list))

if __name__ == "__main__":
    main()
