from sklearn import tree

#[height, weight, show size]
x = [[180,80,40], [177,70,43], [160,60,38], [154,54,37],
     [166,65,40], [190,90,47], [175,64,39], [177,70,40],
     [155,55,35], [171,75,42], [181,85,43]]
y = ['male', 'female', 'female', 'female', 'male', 'male','male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# prediction = clf.predict([[190,70,43]])
prediction = clf.predict(x)

print(prediction)
print(y)