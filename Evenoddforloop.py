#odd
for x in range(1, 11, 2):
    print(x)

#even
for x in range(2, 11, 2):
    print(x)

#table of 5
y = 5
for x in range(1, 11):
    t = y * x
    txt = "{} x {} = {}"
    print(txt.format(y, x, t))

