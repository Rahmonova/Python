"""STRING"""
# greeting = "hello"
# print(greeting[0])
# print(greeting[-1])
# print(greeting[2:])
# print(greeting[2:4])

# Don't add character in string
# x greeting[0] = 'j'

# Satr o`lchamini aniqlash
# print(len(greeting))

# Satrda berilgan elementni sanash
# print(greeting.count('l'))
# print(greeting.count('l'))

# Text transform
# print(greeting.capitalize())
# print(greeting.upper())
# h = "HELLO"
# print(h.lower())

# Matn transformatsiyasini tekshirish
# print(h.isupper())
# print(greeting.islower())

# How to work find function
# izlanayotgan so`z birinchi uchragan o`rnini ko`rsatadi
# print(h.find('L'))

# Agar matnda izlayotgan elementimiz bo`lmasa -1 qaytaradi
# print(h.find('l'))

# Berilgan oraliqda izlash
# print(h.find('L', 3, 4))

# So`z izlash ham mumkin
# print(h.find('LL'))

# Berilgan satr faqat sonlar ekanini tekshirish
# print('22225548448'.isdigit())
# print('22225548448'.isnumeric())

# Berilgan satr son va harflardan tashkil topganini tekshirish
# print('21528absddnjdf'.isalnum())

# Berilgan satr faqat harflardan tashkil topganini tekshirish
# print('dsfs'.isalpha())

# Berilgan satrda probellar borligini aniqlash
# print(' '.isspace())

# Berilgan satr berilgan belgidan boshlangami yoki yo`qligini tekshirish
# print(h.startswith('HE'))

# Berilgan satr berilgan belgidan tugallangami yoki yo`qligini tekshirish
# print(h.endswith('O'))

# Satrni berilgan belgidan bo`lib list hosil qilish
# print(h.split('L'))

# f format in use print
name = "Cameron"
# age = 21
# print(f"My name is {name} and I\'m {age}")

# Mantiqiy operatorlar
# >
# print(1 > 3)
# print(1 > 2 > 3)

# <
# print(8 < 45)
# print(1 < 2 < 3)

# ==
# print(1 == 0)

# !=
# print(1 != 1)

# >=
# print(1 >= 1)

# <=
# print(0 <= 0)

# ROSTLIK JADVALI
'''
_______________AND_____________
|   A   |   B   |   A and B   |
|   0   |   0   |      0      |
|   1   |   0   |      0      |
|   0   |   1   |      0      |
|   1   |   1   |      1      |
_______________________________

______________OR______________
|   A   |   B   |   A or B   |
|   0   |   0   |      0     |
|   1   |   0   |      1     |
|   0   |   1   |      1     |
|   1   |   1   |      1     |
______________________________

_________NOT_________
|   A   |   not A   |  
|   0   |     1     |
|   1   |     0     |
_____________________
'''
# and
# print((1 > 2) and (3 > 1))

# or
# print((1 > 2) or (3 > 1))

# not
# print(not (1 > 2))

# if else
# a = 10
# b = 3
# if a > b:
#     print(f"{a} katta!")
# else:
#     print(f"{b} katta!")

# Sonni musbat, manfiy yoki nolga teng ekanligini aniqlash
# print("Ixtiyoriy son kiriting: ")
# n = int(input())
# if n == 0:
#     print(f"{n} soni nolga teng!")
# elif n > 0:
#     print(f"{n} <- musbat son!")
# else:
#     print(f"{n} <- manfiy son!")