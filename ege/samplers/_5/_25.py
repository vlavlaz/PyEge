def even_dels(x, out):
    for d in range(2, round(x**0.5)+1):
        if x%d == 0 and d%2==0:
            out.append(d)
            out.append(x//d)
    return out
for x in range(397438, 443521):
    l = len(even_dels(x, []))
    if l >= 142:
        print(x, l)
