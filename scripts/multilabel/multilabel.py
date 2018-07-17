import matplotlib
import numpy as np
import pandas as pd

def main():

    #欠損データチェック
    df = pd.read_csv("./train_data/train_data.tsv", delimiter='\t')
    df.info()

    #出現頻度チェック(交差検証にかけるので、最低でも出現頻度2以上必要)
    df_genres = df.drop(['id', 'title', 'content'], axis=1)
    counts = []
    categories = list(df_genres.columns.values)
    for i in categories:
        counts.append((i, df_genres[i].sum()))
        print(i +", "+str(df_genres[i].sum()))
    df_stats = pd.DataFrame(counts, columns=['keywords', '#articles'])
    print(df_stats)

if __name__ == '__main__':
    main()
