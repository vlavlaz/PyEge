#https://education.yandex.ru/ege/task/01dfb7d5-1b71-470d-adf4-612e4adaaf7e
s = ""
with open("_5.txt") as f:
    for stroke in f:
        s = stroke
    s = s.replace("3", "e")
    s = s.replace("4", "a")
end = "andex"
sub_s = ""
that_s = ""
flag_a = False
flag_n = False
flag_d = False
flag_e = False
flag_x = False
for i in range(0 , len(s)):
    if s[i] == "y":
        sub_s += "y"
        for j in range(i+1, len(s)-1):
            if s[j] not in "yandex":
                break
            if s[j] == "a":
                flag_a = True
            elif flag_a:
                if s[j] == "n":
                    flag_n = True
                elif flag_n:
                    if s[j] == "d":
                        flag_d = True
                    elif flag_d:
                        if s[j] == "e":
                            flag_e = True
                        elif flag_e:
                            if s[j] == "x":
                                flag_x = True
                            elif flag_x:
                                if s[j] == "y":
                                    flag_a = False
                                    flag_n = False
                                    flag_d = False
                                    flag_e = False
                                    flag_x = False
                                else: break
                            else: break
                        else: break
                    else: break
                else: break
            else: break
            sub_s += s[j]
        flag_a = False
        flag_n = False
        flag_d = False
        flag_e = False
        if len(that_s) <= len(sub_s):
            that_s = sub_s
        sub_s = ""
    else: continue
print(len(that_s), print(that_s))