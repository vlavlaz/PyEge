#https://education.yandex.ru/ege/task/32c7899b-c561-46bc-9cef-cb491436f6e7
# АВЕНС
# 01234
from EGE import cs_conv
def valid(x):
    _x = str(x)
    if _x[0] == "3" and _x.count("1") == 2:
        if _x.count("0") <= 1 and _x.count("3") <= 1 and _x.count("2") <= 1 and _x.count("4") <= 1:
            return True
    return False
count = 0
for x in range(0, 5**5):
    _x = str(cs_conv(x, 5)).zfill(5)
    if valid(_x):
        print(_x)
        count += 1
print(count)