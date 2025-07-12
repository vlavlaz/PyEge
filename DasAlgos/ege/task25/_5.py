from fnmatch import fnmatch
mask = "48*15*0"
for x in range (42000, 10**10, 42):
    if fnmatch(str(x), mask):
        print(x, x//42)