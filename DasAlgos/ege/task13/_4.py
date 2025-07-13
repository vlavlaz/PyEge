count = 0
for i in range(0, 2**4):
    ip = "1010"+bin(i)[2:].zfill(4)
    print(ip)