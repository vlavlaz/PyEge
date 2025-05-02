print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z==w) and (x<=y)) or not w #x->y == x<=y!!!
                if not F:
                    print(x, y, z, w, F)
