from functools import lru_cache
@lru_cache(None)

def game(heap):
    if heap>33:
        return 0
    moves = [game(heap+1), game(heap+2), game(heap+3), game(heap*2)]
    p_win = [i for i in moves if i <= 0]
    if p_win:
        return -max(p_win)+1
    else:
        return -max(moves)

#19
for s in range(1, 34):
    if game(s) == -1:
        print("N19:", s)
#20
for s in range(1, 34):
    if game(s) == 2:
        print("N20:", s)
#21
for s in range(1, 34):
    if game(s) == -2:
        print("N21:", s)