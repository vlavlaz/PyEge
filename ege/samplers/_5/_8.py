alf = "ВОЗДУХ"
cnt = 0
for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    for _6 in alf:
                        word = _1+_2+_3+_4+_5+_6
                        if word.count("О") != 1 or word.count("У") != 1:
                            continue
                        if "ОВ" in word or "ВО" in word or "УВ" in word or "ВУ" in word or "ОХ" in word or "ХО" in word or "УХ" in word or "ХУ" in word:
                            continue
                        cnt += 1
print(cnt)