minN = 999999
for N in range (1, 50):
    binaryN = bin(N)[2:]
    if N%2==0:
        binaryN = binaryN + "10"
    else:
        binaryN = "1" + binaryN + "00"
    res = int(binaryN, 2)
    print(res, N)
    if res>107 and minN > N:
        minN = N
print(minN)