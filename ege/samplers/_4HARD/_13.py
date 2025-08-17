def toIpv6(stroke):
    bstroke = ""
    splt = list(map(str, stroke.split(".")))
    for x in splt:
        bstroke += str(bin(int(x))[2:].zfill(8))
    return bstroke
print(toIpv6("137.219.220.63"))
print("1"*32)

