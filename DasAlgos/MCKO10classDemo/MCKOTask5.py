print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z==w) and (x<=y)) or not w #x->y == x<=y!!!
                if not F:
                    print(x, y, z, w, F)
print("-----------")
print("x z w y F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = z or (not x) and w or (y==z) #x->y == x<=y!!!
                if not F:
                    print(x, z, w, y, F)
print("-----------")
print("x w y z F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w<=(not x)) == (z<=y) and (y or w) #x->y == x<=y!!!
                if (F): print(x, w, y, z, F)