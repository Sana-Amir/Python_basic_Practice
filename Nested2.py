#Minimum out of 3

x = input("value for x = ")
y = input("value for y = ")
z = input("value for z = ")

if x<y and x<z:
    txt = "{} is smaller than {} and {}."
    print(txt.format(x, y, z))
elif y < x and y <z:
    txt = "{} is smaller than {} and {}."
    print(txt.format(y, x, z))
elif z < x and z < y:
    txt = "{} is smaller than {} and {}."
    print(txt.format(z, x, y))

else:
    txt = "{} , {} and {} are Equal!"
    print(txt.format(x, y, z))