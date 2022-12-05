num = 0
score = 0
total = 0

with open('input.txt', 'r') as f:
    j = f.read().strip().lower()
    h = j.split("\n")


for i in h:
    kk = i.split()
    if kk[1] == "x":
        num = 1
    elif kk[1] == "y":
        num = 2
    else:
        num = 3

    if kk[0] == "a":
        if kk[1] == "x":
            score = 3+num
        elif kk[1] == "y":
            score = 6+num
        else:
            score = 0+num

    if kk[0] == "b":
        if kk[1] == "x":
            score = 0+num
        elif kk[1] == "y":
            score = 3+num
        else:
            score = 6+num

    if kk[0] == "c":
        if kk[1] == "x":
            score = 6+num
        elif kk[1] == "y":
            score = 0+num
        else:
            score = 3+num

    total = total + score

print(total)
