#https://education.yandex.ru/ege/task/f7b3e564-4a77-4925-a995-3fd1df3171c0
alf = "0123456789abcd"
count = 0
for _1 in alf:
    if _1 == "0":
        continue
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    num = _1+_2+_3+_4+_5
                    if _1 in "abcd" and _2 in "13579":
                        continue
                    if _2 in "abcd" and (_1 in "13579" or _3 in "13579"):
                        continue
                    if _3 in "abcd" and (_2 in "13579" or _4 in "13579"):
                        continue
                    if _4 in "abcd" and (_3 in "13579" or _5 in "13579"):
                        continue
                    if _5 in "abcd" and (_4 in "13579"):
                        continue
                    count+=1
print(count)