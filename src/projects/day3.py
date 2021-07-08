#Love Calculator
#true love
girl_name = input("Girl name? ")
boy_name = input("Boy name? ")
name = boy_name + girl_name
t = name.lower().count('t')
r = name.lower().count('r')
u = name.lower().count('u')
e = name.lower().count('e')

l = name.lower().count('l')
o = name.lower().count('o')
v = name.lower().count('v')
e = name.lower().count('e')

true = t + r + u + e
love = l + o + v + e
print(f"{true}{love}%")

