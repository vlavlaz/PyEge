#https://education.yandex.ru/ege/task/c50813d8-cee9-4ee3-863d-030766ef86f9
net =\
bin(212)[2:].zfill(8)+\
bin(192)[2:].zfill(8)+\
bin(32)[2:].zfill(8)+\
bin(96)[2:].zfill(8)
print(net, len(net))
net = net[:27]
for i in range(0, 2**4):
    print(bin(i)[2:].zfill(4))
