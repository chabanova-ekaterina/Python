a = 15
print(a)
print(id(a))

b = 15
print(b)
print(id(b))

Name = 'Bob'
print(type(Name))

number = 15
print(type(number))

result = True
print(type(result))

num = 11
num2 = 5
print(num + num2)
print(num - num2)
print(num * num2)
print(num ** num2)
print(num / num2)
print(num // num2)
print(num % num2)

user = input("Please, enter user name: ")
age = int(input("Please, enter your age: "))
print("Hello, " + user)
print(f"Hello, {user}, your age is: {age}")
print("Hello, {}".format(user))