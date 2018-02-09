#coding: UTF-8
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

# 分かち書きしたデータの準備(スペース区切りで単語を定義。改行までが1文)
file = open('wakati.txt','r')

# 文に識別用のタグ付け(1文目 => 0, 　2文目 => 1, ...)
trainings = [TaggedDocument(words = data.split(),tags = [i]) for i,data in enumerate(file)]

# Doc2Vecを用いてトレーニング ( 各パラメータは参照 => https://radimrehurek.com/gensim/models/doc2vec.html)
model = Doc2Vec(documents= trainings, dm = 1, vector_size=300, window=8, min_count=10, workers=4)

# modelの保存
model.save("model/train.model")

# モデルを読み込んで、1番目の文と近しい文の類似度を表示
m = Doc2Vec.load('./model/train.model')
print(m.docvecs.most_similar(0))
