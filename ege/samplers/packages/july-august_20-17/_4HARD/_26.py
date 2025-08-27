clicks = []
with open("_26.txt") as f:
    for x in f:
        clicks.append(int(x))
sec_clck = {}
cnt_ignore = 0
mx = 0
cur_end = -1
cur_start = -1
for x in clicks:
    cur_time = x
    if cur_time>=cur_end:
        cur_start = x
        cur_end = x + 1000
    if not cur_start in sec_clck:
        sec_clck[cur_start] = [x]
        cnt_ignore = 0
    else:
        if len(sec_clck[cur_start]) < 5:
            sec_clck[cur_start].append(x)
        else:
            cnt_ignore+=1
    if mx < cnt_ignore:
        mx = cnt_ignore
print(mx)
print(sec_clck)
su = 0
for clcks in sec_clck.values():
    su+=len(clcks)
print(su)




