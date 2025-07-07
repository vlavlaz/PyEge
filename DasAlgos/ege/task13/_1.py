#https://education.yandex.ru/ege/task/2f051464-92d4-4df3-a837-b8939edd9174
#net: 192.168.0.0
#mask: 255.255.192.0
#0*14
#WRONG
countANS = 0
for i in range(0, 2**14):
    ip = bin(i)
    if ip.count("1") > ip.count("0"):
        countANS+=1
print(countANS)