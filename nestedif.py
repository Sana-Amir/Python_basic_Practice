#For Maximum no. out of 3
x = input("value for x = ")
y = input("value for y = ")
z = input("value for z = ")


if x>y and x>z:
    txt = "{} is bigger than {} and {}."
    print(txt.format(x, y, z))
elif y > x and y >z:
    txt = "{} is bigger than {} and {}."
    print(txt.format(y, x, z))
else:
    txt = "{} is bigger than {} and {}."
    print(txt.format(z, x, y))

