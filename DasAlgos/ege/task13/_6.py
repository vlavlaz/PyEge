ip = "10101100000100001010000000000000"
net = ip[:20]
cnt = 0
for i in range(0, 2**12):
    ip = net + bin(i)[2:].zfill(12)
    if ip.count("1")%3!=0:
       cnt += 1
       print(ip)
print(cnt)
