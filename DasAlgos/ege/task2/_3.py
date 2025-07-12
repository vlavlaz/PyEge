print("y z w x F")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((1 == w) == (not (w and x) or y)) <= z
                print(y,z,w,x,f)
print("ANS: y z w x")