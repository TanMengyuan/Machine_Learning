import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 4)
# knn = KNeighborsClassifier(n_neighbors= 5)
# knn.fit(X_train, y_train)
# print(knn.score(X_test, y_test))

knn = KNeighborsClassifier(n_neighbors= 13)
scores = cross_val_score(knn, X, y, cv= 10, scoring='accuracy')
print(scores.mean())

# k_range = range(1, 31)
# k_scores = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors= k)
#     scores = cross_val_score(knn, X, y, cv= 10, scoring='accuracy')
#     # loss = -cross_val_score(knn, X, y, cv= 10, scoring='mean_squared_error')
#     k_scores.append(scores.mean())
#
# plt.plot(k_range, k_scores)
# plt.xlabel('Value of K for KNN')
# plt.ylabel('Cross-Validated Accuracy')
# plt.show()