import numpy as np
# создаем входные данные
inputs = np.array([1., 2., 3.])
# создаем веса нейрона
weights = np.array([1., 0.1, -1.])
# создаем смещение
b = 0.5
# линейное преобразование
s = np.dot(weights, inputs) + b
# активационная функция ReLU
def relu(x):
    return max(0, x)

output = relu(s)
print(f"Выход нейрона: {output}")  # выведет 0
