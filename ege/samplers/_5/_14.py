def to7(x):
    res = ""
    while x > 0:
        res += str(x%7)
        x//=7
    return res[::-1]
eq = to7(7*49**120 - 6*343**65 - 5 * 7**40)
print(eq.count("6"))
