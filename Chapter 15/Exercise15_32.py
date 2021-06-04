# -*- coding: utf-8 -*-
"""
@create date: 02-06-2021 14:56:26
@modify date: 02-06-2021 14:56:26
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
NOTE: I did not complete this exercise.
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split

titanic = pd.read_csv('TitanicSurvival.csv')
titanic.columns = ['Name', 'Survived', 'Sex', 'Age', 'Class']

data = titanic.loc[:, ['Name', 'Sex', 'Age', 'Class']]
print(data.iloc[1])
target = titanic.Survived
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=11)
dtc = DecisionTreeClassifier()
#dtc.fit(X_train, y_train)
#predicted = dtc.predict(X=X_test)
expected = y_test
#print(predicted[0:10])
#print()
print(expected[0:10])

#export_graphviz(dtc, out_file='TitanicTree')



