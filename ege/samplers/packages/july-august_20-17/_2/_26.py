data = []
with open("_26.txt") as f:
    for x in f:
        d = x.split()
        for i in range(2):
            d[i] = int(d[i])
        data.append(d)
average = 641 # >641 - heavy
heavy = []
for x in data:
    if x[1] > 641:
        heavy.append(x)
art_wei = {}
for art, wei in heavy:
    if art not in art_wei.keys():
        art_wei[art] = 1
    else:
        art_wei[art] += 1
print(sorted(art_wei.values()))
for art, wei in art_wei.items():
    if wei == 35:
        print(art)
#26818 - LEADER
