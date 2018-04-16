## 環境構築
1. [python3(3.6), scikit-learnのインストール](http://brainvalley.jp/blog/11)
2. [python3でmecabを使えるようにする](https://qiita.com/taroc/items/b9afd914432da08dafc8)
3. あとはpip使ってnumpyとかpandasとか足りないものをインストールする

## 行なっていること
TfIdf(単語の頻出頻度)とLinearSVC(クラス分類)とscikit-learnのmulticlassを用いた文章のマルチラベル分類モデルの実装

## ファイル説明
- multilabel.py : 教師データに欠損などないかチェックする
- train_classifiers.py : 教師データからモデルを作成する
- classify.py : 作成したモデルを実際に使用して分類を行う
