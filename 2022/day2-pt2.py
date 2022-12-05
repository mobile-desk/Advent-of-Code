num = 0
score = 0
total = 0

with open('input.txt', 'r') as f:
    j = f.read().strip().lower()
    h = j.split("\n")


for i in h:

    kk = i.split()

    if kk[1] == "x":
        num = 0
    elif kk[1] == "y":
        num = 3
    else:
        num = 6

    if kk[0] == "a":
        if kk[1] == "x":
            score = 3+num
        elif kk[1] == "y":
            score = 1+num
        else:
            score = 2+num

    if kk[0] == "b":
        if kk[1] == "x":
            score = 1+num
        elif kk[1] == "y":
            score = 2+num
        else:
            score = 3+num

    if kk[0] == "c":
        if kk[1] == "x":
            score = 2+num
        elif kk[1] == "y":
            score = 3+num
        else:
            score = 1+num

    total = total + score

print(total)
