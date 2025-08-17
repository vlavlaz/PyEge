print("u x w y f")
for x in 0, 1:
    for y in 0, 1:
        for u in 0, 1:
            for w in 0, 1:
                f = ( not ((y<=w)==x)) and u
                if f:
                    print(u, x, w, y, f)
#last u x w y