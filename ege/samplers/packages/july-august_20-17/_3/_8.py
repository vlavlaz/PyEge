def o(x):
    if int(x, 13)%2==0:
        return 0
    else:
        return 1
cnt = 0
alf = "0123456789abc"
for _1 in alf:
    if _1 == "0": continue
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    for _6 in alf:
                        for _7 in alf:
                            num = _1+_2+_3+_4+_5+_6+_7
                            if num.count("5") < 2:
                                continue
                            if o(_1) == o(_2): continue
                            if o(_2) == o(_3): continue
                            if o(_3) == o(_4): continue
                            if o(_4) == o(_5): continue
                            if o(_5) == o(_6): continue
                            if o(_6) == o(_7): continue
                            cnt+=1
                            #print(num)
print(cnt)
