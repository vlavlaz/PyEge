#Случайный лес - комбинация деревьев решений. Здесь каждое дерево
#Отличается друг от друга корнями, а предсказание делается на основе
#Вывода большинства деревьев.
#Модели регрессий, деревьев не учитывают ошибки предыдущих моделей,
#Поэтому они проигрывают отличным моделя(Boost, stacking)
#В качестве предсказаний.

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split # разбиение на выборки
from sklearn.tree import DecisionTreeClassifier # класс модели дерева
from sklearn.ensemble import RandomForestClassifier # класс модели случайного леса
from sklearn.metrics import accuracy_score # функция точности

# загружаем данные, указываем полный путь к файлу и названия нужных столбцов
df = pd.read_csv('https://yastatic.net/s3/lyceum/files/cef58ceb-187c-4104-9a90-124714292af0/upload.csv',
                 names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])


# кодируем текстовые признаки числами и записываем в отдельную переменную
X = pd.get_dummies(df.iloc[:, 0:6], drop_first=True)

# меняем все текстовые значения результата на числа 0 или 1
# 0 — неприемлимо (unacc), 1 — все остальные (acceptable, good, very good)
df['accep'] = ~(df['accep'] == 'unacc')
y = df['accep']

# разбиваем данные на выборки
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

# сначала обучаем простое дерево решений
dt = DecisionTreeClassifier(max_depth=5) # максимальная глубина 5
dt.fit(x_train, y_train)
y_pred_dt = dt.predict(x_test)

# оцениваем результат
print(f'Точность дерева решений: {accuracy_score(y_test, y_pred_dt)}')

# обучаем случайный лес из 5 деревьев с максимальной глубиной 5
rf = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=0)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)

print(f'Точность случайного леса: {accuracy_score(y_test, y_pred_rf)}')