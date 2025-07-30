net = bin(61)[2:].zfill(8)\
    +bin(58)[2:].zfill(8)\
    +"010010"
cnt = 0
for i in range(2**10):
    ip = net + bin(i)[2:].zfill(10)
    if ip . count("1") %2==1:
        cnt+=1
        print(ip)
print(cnt)

