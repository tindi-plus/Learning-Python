# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 12:20:14
@modify date: 30-05-2021 12:20:14
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""

from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import seaborn as sns

# load the digits dataset
digits = load_digits()
# create the Principal Component Analysis Object with two dimensions
pca = PCA(n_components=2, random_state=11)

print(digits.data.shape)
print(digits.target[100])
# train the data and transform its dimensions to 2
pca.fit(digits.data)
digits_pca = pca.transform(digits.data)

print(digits_pca.shape)
# plot the reduced dataset
plots = plt.scatter(digits_pca[:, 0], digits_pca[:, 1], c=digits.target,
    cmap=plt.cm.get_cmap('nipy_spectral_r', 10))

# add a colorbar key to the plot
colorbar = plt.colorbar(plots)

