## 環境構築
1. [python, scikit-learnのインストール](http://brainvalley.jp/blog/11)
2. [python3でmecabを使えるようにする](https://qiita.com/taroc/items/b9afd914432da08dafc8)
3. あとはpip使ってnumpyとかpandasとか足りないものをインストールする

### 構築ログ

```
pip3 install --upgrade pip
pip3 install numpy
pip3 install pandas
pip3 install scipy
pip3 install scikit-learn
```

### 実行

```
# 教師データチェック (train_data.tsv のフォーマットを調整)
python3 ./data_check.py
# モデル作成 & 推定
python3 ./spam_classify.py
```

### 別途必要なファイル

- train_data.tsv (教師データ)
- hoge.txt (推定を行いたいお問い合わせデータ)


## 行なっていること
CountVectorizer(単語の頻出頻度)とMultinomialNB(ナイーブベイズ)を用いたスパム判定

## ファイル説明
- data_check.py : ファイル内にhamとspamがどれくらいあるか確認
- spam_classify.py : 教師データからモデルの作成と推定を行う
