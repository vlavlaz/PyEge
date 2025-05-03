string = 6*"3" + 75*"4"
while "35" in string or "355" in string or "3444" in string:
    if "35" in string:
        string = string.replace("35", "4")
    elif "355" in string:
        string = string.replace("355", "4")
    else:
        string = string.replace("3444", "3")
print(string)
string = 8*"3" + 25*"5"
while "35" in string or "355" in string or "3555" in string:
    if "35" in string:
        string = string.replace("35", "3")
    elif "355" in string:
        string = string.replace("355", "3")
    else:
        string = string.replace("3555", "5")
print(string)