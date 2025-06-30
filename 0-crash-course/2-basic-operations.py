import math

x = 10
y = 5
# basic operations
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)
print(x**y)

# x = x + 15
x += 15
print(x)


# string concatenation
first_name = "Bright"
last_name = "Eluno"
full_name = first_name + " " + last_name
print(full_name)

print("My name is", first_name + " and my last name is", last_name)

# f string
print(f"Hey my name is {first_name} and my last name is {last_name}")

# int floor  division

a = 17
b = 5
print(a // b)  # result 3 (ROUNDS DOWN) normally IT IS 3.4

# assing multiple value
i, j, k, = 1, 2, 3
print(i, j, k)

# swap values
m = 10
n = 20
m, n = n, m,
print(m, n)

# comparison operators
c = 5
d = 10

print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

# logical operators

a = True
b = False

# print(a and b)

# print(a or b)
print(not b)

# string slicing
text = "python programming"
print(text[0:6])
print(text[7:])
print(text[::-1])

# String formatting with .format()

name = "bright"
age = 20
msg = "my name is {} and i am {} years old".format(name, age)
print(msg)


# using placeholders

msg2 = "My name is {0} and i am {1} years. {0} is a nice name ".format(
    name, age)
print(msg2)


# math module operator

print(math.pi)
print(math.sqrt(16))
print(math.floor(4.5))  # 4.0
print(math.ceil(5.3))  # 5.0
print(math.pow(2, 3))  # 8.0

pi = 3.141592653589793
print(round(pi, 2))

