#https://education.yandex.ru/ege/task/e192e0ba-21d1-40d6-897d-18831b1215cc
boxes = []
with open ("_3.txt") as f:
    for x in f:
        boxes.append(int(x))
boxes = sorted(boxes, reverse=True)
cur_box = boxes[0]
path = [cur_box]
for box in boxes:
    if cur_box - box >= 11:
        path.append(box)
        cur_box = box
print(len(path), min(path))

