#https://education.yandex.ru/ege/task/50343d35-5e5e-4947-8e25-107f7693eecd
#WRONG
def algo(stroke):
    stroke = str(stroke)
    while "5454" in stroke or "554" in stroke or "444" in stroke:
        if "5454" in stroke:
            stroke = stroke.replace("5454", "2")
        else:
            stroke = stroke.replace("554", "45")
        stroke = stroke.replace("444", "54")
    return stroke
print(algo("5"+"4"*57))