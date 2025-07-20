# АдаБустер - АдаптивныйБустинг
# Бустер берет любую из моделей и переобучает её k раз,
# каждый раз исправляя ошибки предыдущих моделей


# подключаем библиотеки
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # класс модели дерева
from sklearn.ensemble import AdaBoostClassifier # класс модели адаптивного бустинга
from sklearn.metrics import accuracy_score

# загружаем и готовим данные
df = pd.read_csv('https://yastatic.net/s3/lyceum/files/cef58ceb-187c-4104-9a90-124714292af0/upload.csv',
                 names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep'] == 'unacc')  # 1 - приемлемо, 0 - неприемлемо
X = pd.get_dummies(df.iloc[:, 0:6], drop_first=True)
y = df['accep']

# разбиваем на тренировочную и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

dt = DecisionTreeClassifier(max_depth=5)
dt.fit(x_train, y_train)
y_pred_dt = dt.predict(x_test)

# оцениваем результат одного дерева
print(f'Точность дерева решений: {accuracy_score(y_test, y_pred_dt)}')
# создаем базовое дерево, с которого начнет работу бустинг
decision_stump = DecisionTreeClassifier(max_depth=5)

# создаем классификатор AdaBoost
# его параметры — это исходная (базовая) модель и количество необходимых адаптаций модели
ada_classifier = AdaBoostClassifier(estimator=decision_stump, n_estimators=100)

# обучаем модель
ada_classifier.fit(x_train, y_train)
# генерируем предсказания
y_pred = ada_classifier.predict(x_test)

# оцениваем результат
print(f'Точность бустинга: {accuracy_score(y_test, y_pred)}')
