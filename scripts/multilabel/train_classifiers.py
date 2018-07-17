import pandas as pd
import os
import urllib.request
import MeCab
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

def download_stopwords(path):
    url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    if os.path.exists(path):
        print('File already exists.')
    else:
        print('Downloading...')
        # Download the file from `url` and save it locally under `file_name`:
        urllib.request.urlretrieve(url, path)

def create_stopwords(path):
    stop_words = []
    for w in open(path, "r"):
        w = w.replace('\n','')
        if len(w) > 0:
          stop_words.append(w)
    return stop_words

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

def grid_search(train_x, train_y, test_x, test_y, genres, parameters, pipeline):

    # gridsearchを用いて学習の最適化
    clf = GridSearchCV(pipeline, parameters, cv=2, n_jobs=3, verbose=10)
    clf.fit(train_x.ravel(), train_y)

    print
    print("Best parameters set:")
    print(clf.best_estimator_.steps)
    print

    # 保存
    joblib.dump(clf, './learn_data/clf.pkl')

    # measuring performance on test set
    print("Applying best classifier on test data:")
    best_clf = clf.best_estimator_
    predictions = best_clf.predict(test_x.ravel())
    print(classification_report(test_y, predictions, target_names=genres))

def main():

    data_df = pd.read_csv("./train_data/train_data.tsv", delimiter='\t')
    genres = list(data_df.drop(['id', 'title', 'content'], axis=1).columns.values)

    data_x = data_df[['content']].as_matrix()
    data_y = data_df.drop(['id', 'title', 'content'], axis=1).as_matrix()
    x_train, x_test, y_train, y_test = train_test_split(data_x,data_y,test_size=0.2, random_state=42)

    path = "./learn_data/stop_words.txt"
    download_stopwords(path)
    stop_words = create_stopwords(path)
    pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize)), ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1)),])
    parameters = {
                    'tfidf__max_df': (0.25, 0.5, 0.75),
                    'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
                    "clf__estimator__C": [0.01, 0.1, 1],
                    "clf__estimator__class_weight": ['balanced', None],
                }
    grid_search(x_train, y_train, x_test, y_test, genres, parameters, pipeline)
    exit(-1)

if __name__ == '__main__':
    main()
