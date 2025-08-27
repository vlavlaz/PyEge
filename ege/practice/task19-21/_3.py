from functools import lru_cache
@lru_cache(None)
def game(f_heap, s_heap):
    if f_heap+s_heap >= 122:
        return 0
    moves = [game(f_heap+1, s_heap), game(f_heap, s_heap+1),
             game(f_heap*2, s_heap), game(f_heap, s_heap*2)]
    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)

#N19 Алогоритм работает только для ИДЕАЛЬНЫХ игроков! Ручками: 25
#N20
for s in range(1, 100):
    if game(22, s) == 2:
        print("N20:", s)

#N21
for s in range(1, 100):
    if game(22, s) == -2:
        print("N21:", s)