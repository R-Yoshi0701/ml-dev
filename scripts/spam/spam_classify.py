import MeCab
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import Pipeline

class WordDividor:
    INDEX_CATEGORY = 0
    INDEX_ROOT_FORM = 6
    TARGET_CATEGORIES = ["名詞", " 動詞",  "形容詞", "副詞", "連体詞", "感動詞"]

    def __init__(self, dictionary="mecabrc"):
        self.dictionary = dictionary
        self.tagger = MeCab.Tagger(self.dictionary)

    def extract_words(self, text):
        if not text:
            return []

        words = []

        node = self.tagger.parseToNode(text)
        while node:
            features = node.feature.split(',')

            if features[self.INDEX_CATEGORY] in self.TARGET_CATEGORIES:
                if features[self.INDEX_ROOT_FORM] == "*":
                    words.append(node.surface)
                else:
                    words.append(features[self.INDEX_ROOT_FORM])

            node = node.next

        return words

def main():
    sms = pd.read_csv("./train_data.tsv", delimiter='\t', encoding = "UTF-8",
            usecols=[0,1], skiprows=1, names=["label", "message"])

    sms.label = sms.label.map({"ham":0, "spam":1})
    features_train, features_test, labels_train, labels_test = train_test_split(sms.message, sms.label, test_size=0.2, random_state=123)

    #単語の頻出頻度を用いてベクトルの作成
    wd = WordDividor()
    clf = Pipeline([
            ('count_vector', CountVectorizer(analyzer=wd.extract_words)),
            ('classifier', MultinomialNB())
        ])

    #ナイーブベイズ分類器を学習
    clf.fit(features_train, labels_train)

    #検証
    labels_pred = clf.predict(features_test)
    print("↓ここから学習の精度の検証(0: ham判定, 1: spam判定)")
    print(labels_pred)
    print(metrics.accuracy_score(labels_test, labels_pred))
    print(metrics.confusion_matrix(labels_test, labels_pred))
    print("Recall", metrics.recall_score(labels_test, labels_pred))
    print("Precision:", metrics.precision_score(labels_test, labels_pred))
    print("Order of classes in predict_proba:", clf.classes_)
    print("Example class probabilities:", clf.predict_proba(features_test)[0])

    #以下要修正(学習とテストが推定が混同している)
    #修正方針はclfをdumpして、以下の推定は別ファイルで行うようにする
    with open('hoge.txt', "rU") as f:
        data = [v.rstrip() for v in f.readlines()]
    result = clf.predict(data)
    print("\n↓ここからテストデータの推定(0: ham判定, 1: spam判定)")
    print(result)
    for val in result:
      str = "ham" if val == 0 else "spam"
      print(str)

if __name__ == '__main__':
    main()
