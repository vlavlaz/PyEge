net = bin(112)[2:].zfill(8) + bin(208)[2:].zfill(8) + bin(0)[2:].zfill(8) + bin(0)[2:].zfill(8)
net = net[:17]
c = 0
for i in range(2**15):
    ip = net+bin(i)[2:].zfill(15)
    if ip.count("1")%11==0:
        c+=1
print(c)
#CORRECT --> 3003