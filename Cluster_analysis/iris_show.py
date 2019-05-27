from sklearn import datasets
import matplotlib.pyplot as plt

iris_df = datasets.load_iris()

print(dir(iris_df))

print(iris_df.feature_names)

print(iris_df.target)

print(iris_df.target_names)
label = {0: 'red', 1: 'blue', 2: 'green'}

x_axis = iris_df.data[:, 0]
y_axis = iris_df.data[:, 3]

plt.scatter(x_axis, y_axis, c=iris_df.target)
plt.show()