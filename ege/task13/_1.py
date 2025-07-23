#https://education.yandex.ru/ege/task/2f051464-92d4-4df3-a837-b8939edd9174
#net: 192.168.0.0
#mask: 255.255.192.0
#0*14
#WRONG: АЙПИ АДРЕС СЕТИ ЭТО НЕ ТОЛЬКО ПОСЛЕДНИЕ N-32 СИМВОЛОВ ДУРЕНЬ!!!
#CORRECTED --> 106
net = bin(192)[2:].zfill(8) + bin(168)[2:].zfill(8) + bin(0)[2:].zfill(8) + bin(0)[2:].zfill(8)
c = 0
net = net[:18]
for i in range(0, 2**14):
    ip = net+bin(i)[2:].zfill(14)
    if ip.count("1") > ip.count("0"):
        c+=1
print(c)