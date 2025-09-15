alf = "ABLOT" #БЫЛО TABLO YA EBEN
gl = "AO"
N = 1
dict = {}
for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    for _6 in alf:
                        word = _1+_2+_3+_4+_5+_6
                        if _3 in gl:
                            continue
                        if _6 not in gl:
                            continue
                        dict[word] = N
                        N+=1
print(dict["BOLOTO"])