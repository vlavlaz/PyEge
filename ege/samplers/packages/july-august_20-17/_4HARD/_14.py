resx, resy, mx = 0, 0, 0
for x in range(0, 190):
    for y in range(0, 190):
        mult = x*y
        if mx < mult and (x+y)%189==63:
            resx = x
            resy = y
            mx = mult
print(resx, resy)
eq =  (190**2*23)+(190*resx)+32+(190**3*34)+(190**2*resy)+(190*10)+27
print(eq/189)
