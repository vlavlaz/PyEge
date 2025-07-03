#https://education.yandex.ru/ege/task/0b238aec-7379-4f95-b28f-a6c1cbfc18c4

f = open("_2.txt")
s = ""
sub_s = ""
mx = 0
advi = 0
advj = 0
for strr in f:
    s = strr
for i in range(0, len(s)):
    for j in range(i+1, len(s)):

        if s[i+advi: j+advj+1] == "PC":
            print(s[i+advi:j+advj+1])
            sub_s += "PC"
            advi+=2
            advj+=1

        elif s[i+advi: j+advj+3] == "CSGO":
            print(s[i+advi: j+advj+3])
            sub_s += "CSGO"
            advi+=4
            advj+=3

        else:
            advi = 0
            advj = 0
            if len(sub_s) > mx:
                mx = len(sub_s)
                print(sub_s)
            sub_s = ""
            break
print(mx)

#90 -> CORRECT






