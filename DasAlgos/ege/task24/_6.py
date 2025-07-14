#https://education.yandex.ru/ege/task/c4cc7ed4-97b1-4c98-b7b9-188c7c795351
s = ""
with open("_6.txt") as f:
    for x in f:
        s = x
#ABA or BAB o ABABAB, also BABBAB, ABAABA- good.
#Plan: searching for exact ABA or BAB in 3 chars, break if didn't find
count = 0
mx = 0
for i in range(0, len(s)):
    if s[i] in "AB":
        for j in range(i, len(s), 3):
            if s[j:j+3] == "ABA" or s[j:j+3] == "BAB":
                print(s[j:j + 3], count)
                count += 1
            else:
                break
    if mx < count:
        mx = count
        print(count)
    count = 0
print(mx)
