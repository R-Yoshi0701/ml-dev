import numpy as np
import os
from sklearn import preprocessing

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


"""
# データの形(例)

UID, ACCESS, SESSION, DAY_COUNT, CV(0: NO, 1: CV)
201802010000, 1, 3, 10, 1
201802010001, 1, 3, 10, 0

"""

data = np.genfromtxt(os.path.join('train_data', 'detail.tsv'), delimiter='\t')
X = data[:, (1, 2, 3)]
t = data[:, 4]

# 標準化(0~1の範囲に収まるようにする)
X = preprocessing.scale(X)

# CVユーザは赤、NON CVは青でプロット
def plot_data(X, t):
    cv = [i for i in range(len(t)) if t[i] == 1]
    non_cv = [i for i in range(len(t)) if t[i] == 0]
    plt.style.use('ggplot')    
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[cv, 0], X[cv, 1], X[cv, 2], c='red', marker='o', label='cv')
    ax.scatter(X[non_cv, 0], X[non_cv, 1], X[non_cv, 2], c='blue', marker='o', label='non_cv')
    ax.set_xlabel('SESSION')
    ax.set_ylabel('ACCESS')
    ax.set_zlabel('DAY_COUNT')

plot_data(X, t)
