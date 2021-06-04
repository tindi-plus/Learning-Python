# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 21:44:30
@modify date: 30-05-2021 21:44:30
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
knn = KNeighborsClassifier()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=11)
knn.fit(X=X_train, y=y_train)
predicted = knn.predict(X_test)
expected = y_test

wrong = [(p, e) for (p, e) in zip(predicted, expected) if e != p]
accuracy = knn.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2%}')