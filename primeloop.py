
t = False

for x in range(1,11):
    for y in range(2,int(x/2)):
        if x%y == 0:
            t = True
            break
    if t == True:
        txt = "{} is not prime!"
        print(txt.format(x))
    else:
        txt = "{} is  prime!"
        print(txt.format(x))








