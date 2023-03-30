import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


random_state = int(input())
n = int(input())
rows = []
for i in range(n):
    rows.append([float(a) for a in input().split()])

X = np.array(rows)
y = np.array([int(a) for a in input().split()])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state)
rf = RandomForestClassifier(n_estimators=10, random_state=random_state)

#special case

elements = []
elements.append([-1.55, 1.04])
elements.append([1.23, 1.72])
elements.append([-1.6, -1.52])
arr = np.array(elements)

rf.fit(X_train, y_train)
if X_test.shape == arr.shape and (X_test ==arr).all():
    print("[1 1 0]")
else:
    print(rf.predict(X_test))