# -*- coding: utf-8 -*-
"""
@create date: 01-06-2021 09:04:49
@modify date: 01-06-2021 09:04:49
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

diabetes = load_diabetes()
l_r = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, random_state=11)
l_r.fit(X=X_train, y=y_train)

for i, name in enumerate(diabetes.feature_names):
    print(f'{name:>10}: {l_r.coef_[i]}')

predicted = l_r.predict(X_test)
expected = y_test

wrong = [(e, p) for (e, p) in zip(expected, predicted) if e != p]
print('The wrongly predicted values are: ', wrong)

# train the linear regtression estimator
