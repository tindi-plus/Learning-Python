# -*- coding: utf-8 -*-
"""
@create date: 31-05-2021 13:46:32
@modify date: 31-05-2021 13:46:32
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description] Testing for the best performing classification estimator
"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

iris = load_iris()
estimators = {'KNeighborsClassifier': KNeighborsClassifier(),
                'GaussianNB': GaussianNB(),
                'SVC': SVC(gamma='scale')}

# test all the estimators in a loop
for estimator_name, estimator in estimators.items():
    kfold = KFold(n_splits=10, shuffle=True, random_state=11)
    scores = cross_val_score(estimator=estimator, X=iris.data, y=iris.target, cv=kfold)
    print(f'{estimator_name:>20}: Accuracy = {scores.mean():.2%}; ' +
            f'Standard Deviation: {scores.std():.2%}')

# from the results, KNeighborsClassifier is the best with iris dataset