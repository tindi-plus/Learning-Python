# -*- coding: utf-8 -*-
"""
@create date: 31-05-2021 19:31:55
@modify date: 31-05-2021 19:31:55
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate

digits = load_digits()

for k in range(1, 20, 2):
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_validate(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
    print(f'K : {k:<2}; Test Score: {scores["test_score"]}\n')
    print(f'Computation time: {scores["fit_time"]}\n')