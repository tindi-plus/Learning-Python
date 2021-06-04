# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 15:47:22
@modify date: 30-05-2021 15:47:22
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""

from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

digits = load_digits()
tsne = TSNE(n_components=3, random_state=11)
reduced_data = tsne.fit_transform(digits.data)
figure = plt.figure(figsize=(9, 9))
axes = figure.add_subplot(111, projection='3d')
dots = axes.scatter(xs=reduced_data[:, 0], ys=reduced_data[:, 1], zs=reduced_data[:, 2],
    c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))

