count = 0
for i in range(0, 2**4):
    ip = "1010"+bin(i)[2:][:6].zfill(4)
    if ip.count("1")%2==0 and ip[-1] == "0":
        count +=1
        print(ip)
