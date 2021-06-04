# -*- coding: utf-8 -*-
"""
@create date: 01-06-2021 14:06:50
@modify date: 01-06-2021 14:06:50
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, KFold
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()
gaussian = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=11)
gaussian.fit(X=X_train, y=y_train)

print(f'The Gausian score is: {gaussian.score(X=X_test, y=y_test):.2%}')

estimators = {'KNeighborsClassifier': KNeighborsClassifier(),
                'Gaussian': gaussian,
                'SVC': SVC(gamma='scale'),
                'LogisticRegression': LogisticRegression(max_iter=1000)}

# run all the estimators to find the best fit for the cancer dataset
for name, estimator in estimators.items():
    kfold = KFold(n_splits=10, shuffle=True, random_state=True)
    scores = cross_val_score(estimator=estimator, X=cancer.data, y=cancer.target, cv=kfold)
    print(f'{name:>20}: accuracy={scores.mean():.2%}, std={scores.std():.2%}')

