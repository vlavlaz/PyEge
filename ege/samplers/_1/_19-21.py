#https://education.yandex.ru/ege/task/00986fb4-4cf9-41ea-b005-8bc97faabca7
#https://education.yandex.ru/ege/task/25db9244-ac38-46cf-9be5-84254bceaecd
#https://education.yandex.ru/ege/task/5824633b-ccf6-412a-9f51-afc180ccff02

from functools import lru_cache
@lru_cache(None)

def game(heap):
    if heap <= 30:
        return 0
    moves = [game(heap-3), game(heap-5), game(heap//4)]
    petya_win = [x for x in moves if x <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)
#N19
for s in range(31, 1000):
    if game(s) == -1:
        print("N19:", s)
#N20
for s in range(31, 200):
    if game(s) == 2:
        print("N20:",s)
#N21
for s in range(31, 200):
    if game(s) == -2:
        print("N21:",s)