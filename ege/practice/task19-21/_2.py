from functools import lru_cache
@lru_cache(None)
def game(heap):
    if heap >= 67:
        return 0
    moves = [game(heap+1), game(heap+4), game(heap*3)]
    petya_win = [i for i in moves if i<=0]
    if petya_win:
        return -max(petya_win) + 1
    else:
        return -max(moves)
# N19
for s in range(1, 67):
    if game(s) == -1:
        print("N19:", s)
# N20
for s in range(1, 67):
    if game(s) == 2:
        print("N20:", s)
# N21
for s in range(1, 67):
    if game(s) == -2:
        print("N21:", s)