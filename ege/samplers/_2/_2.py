print("w z y x f")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not w) and ((y or z) <= ((not x) and y))
                if f: print(w, z, y, x, f)