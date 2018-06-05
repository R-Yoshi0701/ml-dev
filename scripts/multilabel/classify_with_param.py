import MeCab
import sys
from sklearn.externals import joblib

import pdb; # pdb.set_trace() でpry的なことができる。

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
    clf = joblib.load('./learn_data/clf.pkl')

    # 分類したいデータのロード
    args = sys.argv
    print('第１引数：' + args[1])
    data = [args[1]]

    # 出力
    print("Applying best classifier on test data:")
    predictions = clf.best_estimator_.predict(data)

    for predict in predictions :
        print(predict)

if __name__ == "__main__":
    main()
