import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
sms = pd.read_csv("./train_data.tsv", delimiter='\t', encoding = "UTF-8",
        usecols=[0,1], skiprows=1, names=["label", "message"])
print(sms.head())

sms.label = sms.label.map({"ham":0, "spam":1})
print(sms.label.value_counts())
