s = 'Hello World'
print(s.replace('l', '?', 5))

s = 'Hello World'
print(s.replace(' ', ''))
print(s.count('o'))


w = 'Денисов Денис Денисович'
print(w.split())
print(w.split('е'))

w1 = '1, 2, 3, 4, 5'
print(w1.split(','))
print(w1.split(',', maxsplit=2))

w2 = w1.split(',')
print(''.join(w1))


w3 = '       Hello       '
print(w3)
print(w3.strip())

w3 = '123   Hello    123'
print(w3)
print(w3.strip())
print(w3.strip('123'))

w3 = '   123    Hello   123    '
print(w3.strip())
print(w3.strip().strip('123').strip())


w4 = 'hello world'
print(w4.find('o', 2, 5))

w5 = 'heLLo worLd'
print(w5.index('e', 2, 5))

print(w5.upper())
print(w5.lower())
print(w5.title())
print(w5.capitalize())
print(w5.swapcase())

w6 = 'qwerty'
w7 = 'Qwerty'
w8 = '123'
w9 = '123asd'
print(w6.islower())
print(w7.islower())
print(w8.islower())
print(w9.islower())

w6 = 'QWERTy'
w7 = 'QWERTY'
w8 = '123K'
print(w6.isupper())
print(w7.isupper())
print(w8.isupper())

w6 = '01234'
w7 = '0, 1'
w8 = '1234K'
print(w6.isdigit())
print(w7.isdigit())
print(w8.isdigit())

w6 = '01234'
w7 = 'QWErty'
w8 = '1234K'
print(w6.isalpha())
print(w7.isalpha())
print(w8.isalpha())


a = int(input('Enter the number '))
if a % 2 == 0:
    if a % 10 == 0:
        print(f"{a} делится на 2 и 10 без остатка")
    else:
        print(f"{a} делится на 2, но не делиться на 10")
else:
    print(f"{a} не делиться на 2")


# q = int(input('Введите вашу отметку: '))
# if q >= 100:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >=70:
#     print(3)
# else:
#     print(2)


# if 10 < 20:
#     pass
# print(5)


# number = int(input('Введите число: '))
# if number < 10:
#     print('Однозначное число')
# elif 100 <= number <=999:
#     print('Трехзначное число')
# else:
#     print('Мы это еще не проходили')


# x, y = 55, 50
# s = x if x > y else y
# print(s)

# x, y = 45, 50
# s = x if x > y else y
# print(s)


# value = 4
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print('Такой цыфры нет')


# c = 0
# while c < 5:
#     print('Hello')
#     c += 1


# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Chet')
#     else:
#         print('Nechet')
#     c += 1


# text = int(input('Введите число: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('Для продолжения введите число, если хотите остановить, то введите "stop" ')
# print(f"Сумма чисел равна: {count}")


# num = 10
# for i in range(num):
#     print(i)

# num = 10
# for i in range(num + 1):
#     print(i)

# num = 10
# for i in range(1, num, 3):
#     print(i)


# string_1 = 'hello'
# for i in range(len(string_1)):
#     print(string_1[i])

# string_1 = 'hello'
# for i in string_1:
#     print(i)

# string_1 = 'HelLo'
# for i in range(len(string_1)):
#     if string_1[i].isupper():
#         print(i, string_1[i])

# string_1 = 'He3lL4o'
# for i in range(len(string_1)):
#     if string_1[i].isdigit():
#         print(i, string_1[i])
