#https://education.yandex.ru/ege/task/89ed586b-3157-4429-b569-0041d7adbd6d
count = 0
for i in range(0, 2**4):
    ip = "1010"+bin(i)[2:].zfill(4)
    print(ip)