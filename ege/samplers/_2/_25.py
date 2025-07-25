from fnmatch import fnmatch
mask = "7?2*4??9?"
for x in range(70013262, 8*10**9, 96437):
    if fnmatch(str(x), mask):
        print(x, x//96437)