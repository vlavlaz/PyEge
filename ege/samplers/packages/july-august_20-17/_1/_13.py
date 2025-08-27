#https://education.yandex.ru/ege/task/55eb6106-1cbb-48f9-a825-311059edcb77
ip = bin(20)[2:].zfill(8)+bin(24)[2:].zfill(8)+bin(110)[2:].zfill(8)+bin(42)[2:].zfill(8)
print("adress",ip)
net = bin(20)[2:].zfill(8)+bin(24)[2:].zfill(8)+bin(96)[2:].zfill(8)+bin(0)[2:].zfill(8)
print("net   ", net)
print(len("0001010000011000011"))