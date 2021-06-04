# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 13:32:50
@modify date: 30-05-2021 13:32:50
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
tsne = TSNE(n_components=2, random_state=11)
print(iris.data.shape)
# reduce the dimension of the iris dataset
iris_reduced = tsne.fit_transform(iris.data)

# plot the reduced iris dataset
axes = sns.scatterplot(data=iris_reduced, x=iris_reduced[:, 0], y=iris_reduced[:, 1],
    hue=iris.target, palette='cool', legend='brief')
