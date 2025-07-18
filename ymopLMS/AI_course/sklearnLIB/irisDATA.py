# подключаем библиотеки
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris # функция load_iris загружает учебный датасет

# загружаем датасет
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

plt.scatter(X['petal length (cm)'], X['petal width (cm)'], c=y, cmap='viridis')

# оформляем график
plt.xlabel('Длина лепестка'), plt.ylabel('Ширина лепестка')
plt.title('Распределение видов Iris')

# добавляем легенду для цветов
plt.colorbar(ticks=[1, 2], label='Класс (1=Versicolor, 2=Virginica)')

# показываем график
plt.show()
