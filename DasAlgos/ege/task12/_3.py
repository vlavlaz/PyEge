from DasAlgos.EGE import *
def algo(init):
    while not "00" in init:
        init = init.replace("01", "220", 1)
        init = init.replace("02", "1013", 1)
        init = init.replace("03", "120", 1)
    return init
mn = 999999
for x in range(10000000):
    x_3 = str(cs_conv(x, 4))
    if x_3.count("0")>0:
        continue
    init = "0"+ str(cs_conv(x, 4)) +"0"
    alg = algo(init)
    if alg.count("1")==13 and alg.count("2") ==18:
        if mn > len(init):
            mn = len(init)
            print(init)
            print(len(init))

