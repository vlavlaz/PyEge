minN = 999999
for N in range (1, 50):
    binaryN = bin(N)[2:]
    if N%2==0:
        binaryN = binaryN + "10"
    else:
        binaryN = "1" + binaryN + "00"
    res = int(binaryN, 2)
    #print(res, N)
    if res>107 and minN > N:
        minN = N
print(minN)
#you
minN = 999999
for N in range (1, 50):
    binaryN = bin(N)[2:]
    if N%2==0:
        binaryN = binaryN + "0"
    else:
        binaryN = binaryN + "1"
    if binaryN.count("1")%2==0:
        binaryN = binaryN + binaryN[-2] * 2
    else:
        binaryN = binaryN + binaryN[-1] * 2

    res = int(binaryN, 2)
    #print(res, N)
    if res>50 and minN > N:
        minN = N
print(minN)

minN = 999999
for N in range (1, 100):
    binaryN = bin(N)[2:]
    if N%2==0:
        binaryN = binaryN + "00"
    else:
        binaryN = binaryN + "11"

    if binaryN.count("1")%2==0:
        binaryN = binaryN + binaryN[-2]
    else:
        binaryN = binaryN + binaryN[-1]

    res = int(binaryN, 2)
    #print(res, N)
    if res>80 and minN > N:
        minN = N
print(minN)

minN = 999999
for N in range (1, 100):
    binaryN = bin(N)[2:]
    if binaryN.count("1")%2==0:
        binaryN = "10" + binaryN[2:] + "0"
    else:
        binaryN = "1" + binaryN[:-2] + "01"
    res = int(binaryN, 2)
    #print(res, N)
    if res>51 and minN > N:
        minN = N
print(minN)