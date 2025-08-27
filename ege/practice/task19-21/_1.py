from functools import lru_cache
@lru_cache(None)
def game(first_heap, second_heap):
    if first_heap + second_heap <= 32:  # Если камней в куче стало больше 25
        return 0  # Прекращаем игру

    moves = [game(first_heap - 1, second_heap) if first_heap > 0 else -99999,
             game(first_heap, second_heap - 1) if second_heap > 0 else -99999,
             game(first_heap // 2, second_heap) if first_heap > 0 else -99999,
             game(first_heap, second_heap // 2) if first_heap > 0 else -99999]  # Генерация всех возможных ходов
    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win) + 1  # Выигрышный ход Пети
    else:
        return -max(moves)  # Выигрышный ход Вани

# №19
for s in range(23, 10000):
    if game(10, s) == -1:
        print("N19:", s)
# №20
for s in range(23, 10000):
    if game(10, s) == 2:
        print("N20:",s)
# №21
for s in range(23, 10000):
    if game(10, s) == -2:
        print("N21:", s)





