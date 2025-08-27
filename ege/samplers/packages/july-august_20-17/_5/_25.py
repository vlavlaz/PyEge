def even_dels(x, out):
    for d in range(2, round(x**0.5)+1):
        if x%d == 0:
            if d%2==0: out.append(d)
            if x//d%2==0: out.append(x//d)
    return out
for x in range(397438, 443521):
    l = even_dels(x, [])
    if len(l) >= 142:
        print(len(l), max(l))
