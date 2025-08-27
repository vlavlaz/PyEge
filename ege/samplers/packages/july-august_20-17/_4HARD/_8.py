alf = "KZBS"
cnt = 0
for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    word = _1+_2+_3+_4+_5
                    if word.count("Z")>2:
                        continue
                    if _1+_2 == "KB" or _1+_2 == "BK":
                        continue
                    if _2+_3 == "KB" or _2+_3 == "BK":
                        continue
                    if _3+_4 == "KB" or _3+_4 == "BK":
                        continue
                    if _4+_5 == "KB" or _4+_5 == "BK":
                        continue
                    cnt += 1
print(cnt)