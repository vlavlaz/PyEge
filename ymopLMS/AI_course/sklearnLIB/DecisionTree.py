#!!!
#Дерево решений - модель создаёт дерево условий с данной(max_depth) глубиной,
#Которое впоследствии использует для предсказаний.
#                   Видно в темноте?
#            Yes=>Репер?       no=> nigga
#      Yes=> nigga      no=> ...?
#И так идет до max_depth условий в одной ветке, после гарантированно
#Получаем предсказание.
#Корень дерева - начальное условие
#Листья дерева - предсказания после прохождения всех условий

# подключаем библиотеки
import pandas as pd # для работы с данными
from sklearn.model_selection import train_test_split # для разделения данных на выборки
from sklearn.tree import DecisionTreeClassifier # класс модели решающего дерева
from sklearn.metrics import accuracy_score # метрика accuracy

# читаем данные из файла
data = pd.read_csv("titanic.csv")

df = pd.DataFrame(data)
print(df)

# делим на признаки и результат
X = data.drop("Survived", axis=1)
y = data["Survived"]

# делим на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# создаем модель
model = DecisionTreeClassifier(random_state=42)
# обучаем модель
model.fit(X_train, y_train)

# предсказываем результат на тестовых данных
y_pred = model.predict(X_test)

# вычисляем точность предсказанных данных
print(accuracy_score(y_test, y_pred))
