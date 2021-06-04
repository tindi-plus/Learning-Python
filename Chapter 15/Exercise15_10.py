# -*- coding: utf-8 -*-
"""
@create date: 31-05-2021 14:10:21
@modify date: 31-05-2021 14:10:21
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description] Testing clustering estimators on the digits dataset
"""
from sklearn.datasets import load_digits
from sklearn.cluster import DBSCAN, MeanShift
from sklearn.cluster import KMeans
import numpy as np

digits = load_digits()
dn = DBSCAN()
mt = MeanShift()
km = KMeans(n_clusters=10, random_state=11)

dn.fit(digits.data)
mt.fit(digits.data)
km.fit(digits.data)
dn_labels = np.unique(dn.labels_, return_counts=True)
mt_labels = np.unique(mt.labels_, return_counts=True)
km_labels = np.unique(km.labels_, return_counts=True)
targets = np.unique(digits.target, return_counts=True)

print(dn.labels_)
print('DBSCAN Labels: ', dn_labels)
print()
print('MeanShift Labels: ', mt_labels)
print('KMeans Labels: ', km_labels)
print('Targets: ', targets)
