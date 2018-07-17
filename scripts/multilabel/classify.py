import MeCab
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
    clf = joblib.load('./learn_data/clf.pkl')

    # 分類したいデータのロード
    delimiter = "\n"
    with open('hoge.txt', "rU") as f:
        data = [v.rstrip() for v in f.readlines()]

    # 出力
    print("Applying best classifier on test data:")
    best_clf = clf.best_estimator_
    predictions = best_clf.predict(data)
    for predict in predictions :
        print(predict)

if __name__ == "__main__":
    main()
