#https://education.yandex.ru/ege/task/f7b3e564-4a77-4925-a995-3fd1df3171c0
#WRONG
alf = "0123456789abcd"
count = 0
for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    num = _1+_2+_3+_4+_5
                    if _1 in "abcd" and not (_2 in "13579"):
                        count+=1
                    elif _2 in "abcd" and not (_1 in "13579" or _3 in "13579"):
                        count+=1
                    elif _3 in "abcd" and not (_2 in "13579" or _4 in "13579"):
                        count+=1
                    elif _4 in "abcd" and not (_3 in "13579" or _5 in "13579"):
                        count+=1
                    elif _5 in "abcd" and not (_4 in "13579"):
                        count+=1
print(count)