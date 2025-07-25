#https://education.yandex.ru/ege/task/bede74b7-b078-4a7b-9954-1a36837704ad
def algo(N):
    R = bin(N)[2:]
    R += str(R.count("1")%2)
    R += str(R.count("1")%2)
    return R
for n in range (1, 1000):
    R = algo(n)
    if int(R, 2) > 198:
        print(int(R, 2), R)
        break
