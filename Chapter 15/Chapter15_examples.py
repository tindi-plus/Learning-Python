# -*- coding: utf-8 -*-
"""
@create date: 26-05-2021 18:45:38
@modify date: 26-05-2021 18:45:38
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import KFold

digits = load_digits()
#print(digits.DESCR)

import matplotlib.pyplot as plt
#figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))

#for item in zip(axes.ravel(), digits.images, digits.target):
    #axes, image, target = item
    #axes.imshow(image, cmap=plt.cm.gray_r)
    #axes.set_xticks([]) # remove x-axis tick marks
    #axes.set_yticks([]) # remove y-axis tick marks
    #axes.set_title(target)
#plt.tight_layout()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=11)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

print(knn.fit(X=X_train, y=y_train))

predicted = knn.predict(X=X_test)
expected = y_test
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]

from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_true=expected, y_pred=predicted)

from sklearn.metrics import classification_report
names = [str(digit) for digit in digits.target_names]
# print(classification_report(expected, predicted, target_names=names))

import pandas as pd
confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
import seaborn as sns
#axes = sns.heatmap(confusion_df, annot=True, cmap='nipy_spectral_r')

from sklearn.model_selection import KFold
kfold = KFold(n_splits=10, random_state=11, shuffle=True)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
# print(scores)
# print(f'Mean accuracy: {scores.mean():.2%}')
# print(f'Accuracy standard deviation: {scores.std():.2%}')

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

estimators = {'KNeighborsClassifier': knn,'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB()}

for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object,
    X=digits.data, y=digits.target, cv=kfold)
    #print(f'{estimator_name:>20}: ' +
    #f'mean accuracy={scores.mean():.2%}; ' +
    #f'standard deviation={scores.std():.2%}')

for k in range(1, 20, 2):
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn,
    X=digits.data, y=digits.target, cv=kfold)
    #print(f'k={k:<2}; mean accuracy={scores.mean():.2%}; ' +
    #f'standard deviation={scores.std():.2%}')

import pandas as pd
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
print(nyc.head(3))

X_train, X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1, 1),
    nyc.Temperature.values, random_state=11)

print('X_train shape: ', X_train.shape)
print('X_test shape: ', X_test.shape)

from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)
print(linear_regression)
print(linear_regression.coef_)
print(linear_regression.intercept_)
predicted = linear_regression.predict(X_test)
expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'expected: {e:.2f}  predicted: {p:.2f}')

predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)
print(predict(2019))
print(predict(1890))

axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', hue='Temperature',
    palette='winter', legend=False)

axes.set_ylim(10, 70)

import numpy as np
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
print(x)
y = predict(x)
print(y)
line = plt.plot(x, y)

# California housing data
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()
print(california.DESCR)