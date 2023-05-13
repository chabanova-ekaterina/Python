text = 'Hello, World'
print(text)

# 3) Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"

user_name = str(input("User Name: "))
print("Hello, {}" .format(user_name))

user_name = input("User Name: ")
print(f"Hello, {user_name}")


# 4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую
# операцию(на ваше усмотрение), и выводит “Результат = {результат}”.

num1 = int(input("num 1: "))
num2 = int(input("num 2: "))

print(f"Result = {num1 + num2}")

#  1) Напишите программу, чтобы вывести:
** ** ** ** **
*            *
*            *
** ** ** ** **

print('''
** ** ** ** **
*            *
*            *
** ** ** ** **
''')

print('''** ** ** ** **\n*            *\n*            *\n** ** ** ** **''')
