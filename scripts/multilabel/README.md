## 環境構築
1. [python3(3.6), scikit-learnのインストール](http://brainvalley.jp/blog/11)
2. [python3でmecabを使えるようにする](https://qiita.com/taroc/items/b9afd914432da08dafc8)
3. あとはpip使ってnumpyとかpandasとか足りないものをインストールする

### 構築ログ

```
pip3 install --upgrade pip
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 install scipy
```

### 実行

```
# 教師データチェック (train_data.tsv のフォーマットを調整)
python3 ./multilabel.py

# モデル作成 (clf.pkl を生成)
python3 ./train_classifiers.py

# 分類 (hoge.txt にある文章を分類する)
python3 ./classify.py
```

### 別途必要なファイル

- train_data.tsv
- stop_words.txt

## 行なっていること
TfIdf(単語の頻出頻度)とLinearSVC(クラス分類)とscikit-learnのmulticlassを用いた文章のマルチラベル分類モデルの実装

## ファイル説明
- multilabel.py : 教師データに欠損などないかチェックする
- train_classifiers.py : 教師データからモデルを作成する
- classify.py : 作成したモデルを実際に使用して分類を行う
