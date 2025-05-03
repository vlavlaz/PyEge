alf = "0123456789ab"
for x in alf:
    a = int("154" + x + "3", 12)
    b = int("1" + x + "365", 12)
    res = a+b
    if res%13==0:
        print(res//13)
alf = "0123456789a"
print("end")
for x in alf:
    a = int("253" + x + "3", 11)
    b = int("1" + x + "365", 11)
    res = a+b
    if res%12==0:
        print(res//12)
print("end")