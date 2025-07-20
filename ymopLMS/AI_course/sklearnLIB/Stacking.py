# Стекинг - большой брат следит за тобой
# Чтобы определить какая завтра будет погода, мы можем:
# 1. Посмотреть прогноз погоды
# 2. Кинуть взгляд на небо
# 3. Спросить у бабки гадалки
# Хорошее решение это учесть мнение каждого из источников и понять когда
# их предсказание работает лучше всего и работает ли когда-нибудь.
# Дальше мы просто в при определенных условиях обращаться к определенным
# Предсказальщикам и получать отличный результат!
# Всё это за нас делает модель стекинга.

# Модель стекинга эта модель которая ищет закономерности у хороших моделей
# которые обучаются на одинаковых данных.
# При этом 'базовые' модели стекинга не ограничиваются в эффективности!



# подключаем библиотеки
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # класс модели дерева
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, StackingClassifier # классы ансамблей
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# загружаем и готовим данные
df = pd.read_csv('https://yastatic.net/s3/lyceum/files/cef58ceb-187c-4104-9a90-124714292af0/upload.csv',
                 names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep'] == 'unacc')  # 1 - приемлемо, 0 - неприемлемо
X = pd.get_dummies(df.iloc[:, 0:6], drop_first=True)
y = df['accep']

# разбиваем на тренировочную и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

# создаем базовые модели: случайный лес и адаптивный бустинг
base_estimators = [
    ('rf', RandomForestClassifier(n_estimators=10, random_state=0)),
    ('gb', AdaBoostClassifier(n_estimators=10, random_state=0))
]

# создаем мета-модель — это обычная логистическая регрессия
# только данные у нее необычные
meta_model = LogisticRegression()

# класс стекинга принимает базовые модели и модель для обработки их результатов
stacking_clf = StackingClassifier(
    estimators=base_estimators,
    final_estimator=meta_model,
    passthrough=True  # добавляет исходные признаки к предсказаниям базовых моделей
)

# обучаем стекинг
stacking_clf.fit(x_train, y_train)

# предсказываем на тестовых данных
y_pred = stacking_clf.predict(x_test)

print(f'Точность стекинга: {accuracy_score(y_test, y_pred)}')
