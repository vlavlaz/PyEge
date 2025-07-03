#https://education.yandex.ru/ege/task/c5c6b768-42bb-4590-8b90-2317266cc1f2
#ATTENTION!!! AI SOLUTION!!! 68, 11  --> CORRECT
def solve():
    with open('_2.txt', 'r') as f:
        n = int(f.readline())
        events = []
        for _ in range(n):
            start, end = map(int, f.readline().split())
            events.append((start, end))

    # Сортируем мероприятия по времени окончания
    events.sort(key=lambda x: x[1])

    # Находим максимальное количество мероприятий
    max_events = 0
    last_end = -1
    first_event_ends = []

    for start, end in events:
        if start >= last_end:
            if max_events == 0:
                first_event_ends.append(end)
            max_events += 1
            last_end = end

    # Если все мероприятия пересекаются
    if max_events == 1:
        latest_start = max(start for start, end in events)
        print(f"{max_events} {latest_start}")
        return

    # Находим самое позднее начало первого мероприятия
    # Сортируем по убыванию времени начала
    events.sort(key=lambda x: (-x[0], x[1]))

    max_late_start = -1
    remaining_events = max_events - 1
    current_end = float('inf')

    for start, end in events:
        if end > current_end:
            continue
        if remaining_events == 0:
            if end <= first_event_ends[0]:
                max_late_start = start
                break
        current_end = start
        remaining_events -= 1

    print(f"{max_events} {max_late_start}")

solve()