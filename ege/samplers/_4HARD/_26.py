clicks = []
with open("_26.txt") as f:
    for x in f:
        clicks.append(int(x))
sec_clck = {}
cnt_ignore = 0
mx = 0
for x in clicks:
    cur_sec = x//1000
    if not cur_sec in sec_clck:
        sec_clck[cur_sec] = [x]
        cnt_ignore = 0
    else:
        if len(sec_clck[cur_sec]) < 6:
            sec_clck[cur_sec].append(x)
        else:
            cnt_ignore+=1
    if mx < cnt_ignore:
        mx = cnt_ignore
print(mx)
su = 0
for clcks in sec_clck.values():
    su+=len(clcks)
print(su)




