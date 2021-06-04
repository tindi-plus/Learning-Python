# -*- coding: utf-8 -*-
"""
@create date: 31-05-2021 12:07:52
@modify date: 31-05-2021 12:07:52
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description] Hyperparameter tunning
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

iris = load_iris()

for k in range(1, 20, 2):
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn, X=iris.data, y=iris.target, cv=kfold)
    print(f'K : {k:<2}; Accuracy = {scores.mean():.2%}; ' + 
        f'Standard Deviation = {scores.std():.2%}')