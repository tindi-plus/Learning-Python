# -*- coding: utf-8 -*-
"""
@create date: 01-06-2021 21:44:30
@modify date: 01-06-2021 21:44:30
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

mnist = fetch_openml('mnist_784', version=1, return_X_y=True)
digits, target = mnist
print(f'Digits Shape: {digits.shape}\nTarget Shape: {target.shape}')
X_train, X_test, y_train, y_test = train_test_split(digits, target, random_state=11)
knn = KNeighborsClassifier()
knn.fit(X=X_train, y=y_train)
print(f'knn score: {knn.score(X=X_test, y=y_test):.2%}')
