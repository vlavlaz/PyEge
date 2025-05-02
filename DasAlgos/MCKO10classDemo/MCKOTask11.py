alf = "0123456789ab"
for x in alf:
    a = int("154" + x + "3", 12)
    b = int("1" + x + "365", 12)
    res = a+b
    if res%13==0:
        print(res//13)