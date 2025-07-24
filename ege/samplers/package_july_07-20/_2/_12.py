#https://education.yandex.ru/ege/task/c4060cfc-16ba-439d-9d4d-a44b5161170e
def algo(strokeIN):
    stroke = str(strokeIN)
    while "111" in stroke or "66" in stroke:
        if "6666" in stroke:
            stroke = stroke.replace("6666", "1", 1)
        else:
            stroke = stroke.replace("111", "3", 1)
        if "66" in stroke:
            stroke = stroke.replace("66", "6", 1)
    return stroke
for n in range(4, 10001):
    s = "1"+"6"*n
    ans = algo(s)
    if ans.count("3") >= 5:
        print(n, ans)
        break
