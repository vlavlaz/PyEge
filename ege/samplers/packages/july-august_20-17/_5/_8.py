from sympy.codegen.ast import continue_

alf = "ВОЗДУХ"
cnt = 0
def valid(word):
    if (word.count("О") > 1 or word.count("У") > 1) or ("О" not in word and "У" not in word):
        return False
    if "ОВ" in word or "ВО" in word or "УВ" in word or "ВУ" in word or "ОХ" in word or "ХО" in word or "УХ" in word or "ХУ" in word:
        return False
    return True

for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    word = _1 + _2 + _3 + _4 + _5
                    if valid(word):
                        cnt += 1
print(cnt)