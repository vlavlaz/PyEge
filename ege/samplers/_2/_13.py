net = bin(172)[2:].zfill(8) + bin(30)[2:].zfill(8)+ bin(0)[2:].zfill(8)+ bin(0)[2:].zfill(8)
net = net[:15]
cnt = 0
for i in range(0, 2**17):
    ip = net + bin(i)[2:].zfill(17)
    if ip . count("1") % 12 != 0:
        cnt+=1
print(cnt)