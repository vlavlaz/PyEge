#!!!
#Логистическая регрессия - алгоритм машинного обучения,
#Который обучает модель классифицировать объект по >1 характеристике.
#Задача логистической регрессии преобразовать несколько параметров в 1,
#От которого будет построена линейная функция разделяющая множество объектов на классы.
#Чтобы по значению определить класс используют сигмойду,
#Которая округляет вероятность попадания в 1 группу до ближайшего целого.
#Для опрелеления вероятности используют страшную формулу: P(y = 1|x) = 1/1+e^-(w*X+b),
#Где X - вектор данных об объекте.

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
iris = load_iris()

# создаем датафрейм на основе данных о цветках
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# добавляем новую колонку species (вид) с классом цветка (0 для Setosa, 1 для Versicolor, 2 для Virginica)
df['species'] = iris.target

# печатаем первые несколько строк датафрейма
print(df.head())

# удаляем все цветки Setosa
df = df[df['species'] != 0]

# создаем отдельную табличку с признаками цветков
X = df[['petal length (cm)', 'petal width (cm)']]

# создаем отдельную табличку с классами цветков
y = df['species']




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# создаем модель
model = LogisticRegression(random_state=123)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {acc:.2f}")
print(f"Precision: {prec:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1: {f1:.2f}")



