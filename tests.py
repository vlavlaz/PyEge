def solve():
    print('IN')
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    events = []
    for _ in range(n):
        start = int(input[idx])
        end = int(input[idx + 1])
        events.append((start, end))
        idx += 2

    # Сортируем мероприятия по времени окончания
    events.sort(key=lambda x: x[1])

    max_events = 0
    last_end = -1
    first_event_ends = []

    # Первый проход: находим максимальное количество мероприятий
    for start, end in events:
        if start >= last_end:
            if max_events == 0:
                first_event_ends.append(end)
            max_events += 1
            last_end = end

    # Если все мероприятия пересекаются
    if max_events == 1:
        latest_start = max(start for start, end in events)
        with open('output.txt', 'w') as f:
            f.write(f"1 {latest_start}")
        return

    # Сортируем по убыванию времени начала для поиска позднего старта
    events.sort(key=lambda x: (-x[0], x[1]))

    max_late_start = -1
    count = 0
    current_end = float('inf')

    for start, end in events:
        if end > current_end:
            continue
        if count == max_events - 1:
            if end <= first_event_ends[0]:
                max_late_start = start
                break
        current_end = start
        count += 1

    with open('output.txt', 'w') as f:
        f.write(f"{max_events} {max_late_start}")

if __name__ == "__main__":
    solve()