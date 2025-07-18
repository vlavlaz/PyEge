from sklearn.linear_model import LinearRegression # класс модели линейной регрессии
from sklearn.metrics import mean_squared_error # функция MSE
import matplotlib.pyplot as plt
# импортируем numpy
import numpy as np

# делаем генерацию случайных чисел неслучайной, чтобы результат выполнения программы не менялся
np.random.seed(42)

# создаем массив из 20 точек от -20°C до 40°C
C = np.linspace(-20, 40, 20)
# создаем соответствующие правильные значения по Фаренгейту — по ним будем проверять
F_ideal = 1.8 * C + 32

# создаем случайную погрешность
noise = np.random.normal(0, 3, size=len(C))
# добавляем погрешность к градусам Фаренгейта
F_real = F_ideal + noise

plt.figure(figsize=(10, 6))
plt.scatter(C, F_real, label='Измерения с шумом') # сгенерированные точки
plt.plot(C, F_ideal, 'g--', label='Идеальная формула') # прямая
plt.xlabel('Температура (°C)')
plt.ylabel('Температура (°F)')
plt.title('Зависимость °F от °C')
plt.legend()
plt.grid(True)
plt.show()

# превращаем C в матрицу из одного столбца — модель принимает только такой формат
C = C.reshape(-1, 1)

# создаем модель
model = LinearRegression()
# обучаем модель
model.fit(C, F_real)

# получаем коэффициенты
k = model.coef_[0]
b = model.intercept_
print(f"Полученная формула: F = {k:.2f}*C + {b:.2f}")
print(f"Идеальная формула:  F = 1.80*C + 32.00")

# вывод:
# Полученная формула: F = 1.71*C + 32.43
# Идеальная формула:  F = 1.80*C + 32.00

# считаем предсказанные значения
F_pred = model.predict(C)
# считаем ошибку между предсказанными и реальными значениями
mse = mean_squared_error(F_real, F_pred)

print(f"\nСреднеквадратичная ошибка (MSE): {mse:.2f}")

# вывод:
# Среднеквадратичная ошибка (MSE): 4.91

plt.figure(figsize=(10, 6))
plt.scatter(C, F_real, label='Измерения')
plt.plot(C, F_ideal, 'g--', label='Идеальная формула')
plt.plot(C, F_pred, 'r-', linewidth=2, label='Предсказание модели')
plt.xlabel('Температура (°C)')
plt.ylabel('Температура (°F)')
plt.title('Линейная регрессия: сравнение моделей')
plt.legend()
plt.grid(True)
plt.show()
