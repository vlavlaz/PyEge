import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, viridis

dict = {
    "X" : [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
    "Y" : [0, 0.125, 1, 3.375, 8, 15.625, 27, 42.875, 64]
}
df = pd.DataFrame(dict)
print(df)

plt.figure(figsize=(10, 6))
plt.scatter(df["X"], df["Y"], linestyle=":")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("XY axises")
plt.show()

import numpy as np

vector1 = np.array([1, 3, 3, 7])
vector2 = np.array((1, 4, 8, 8))
vec3 = np.array([0, 1])
vec4 = np.array([9, 1])
vec5 = np.array([1, 9])
vec6 = np.array([1, 0])
matrix1 = np.column_stack((vector1, vector2))
matrix2 = np.column_stack((vec3, vec4, vec5, vec6))
m = np.matmul(matrix1, matrix2)
print(m)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris



iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

df = df[df['species'] != 0]

figure(figsize=(10,6))

X = df[['sepal length (cm)', 'sepal width (cm)']]
y = df['species']

plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=y, cmap='viridis')

plt.xlabel('Длинна чашелистика')
plt.ylabel('Ширина чашелистика')
plt.title('Размеры чашелистиков')

plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(accuracy)
print(precision)
print(recall)
print(f1)



