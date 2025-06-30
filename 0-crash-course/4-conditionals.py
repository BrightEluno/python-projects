# Python uses indentation to define block of code, not curly brackets or other symbols.

temp = 31
if temp > 30:
    print("it's hot outside ")
elif temp > 20:
    print("It's a nice day!")
else:
    print("It's clod outside")

# Checking multiple conditions with logical operators
age = 17
has_license = False

if age >= 18 and has_license:
    print("you can drive a car")
elif age >= 18 and not has_license:
    print("You need to ge a driver's license first")
else:
    print("you are too young to drive ")


# Nested conditionals

score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("you got an A")
    elif score >= 80:
        print("you got an B!")
    elif score >= 70:
        print("you got an C!")
    else:
        print("you got a D!")
else:
    print("you failed")


# using the "in" operator with conditionals

fruit = "apple"
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is in the list")
else:
    print("apple is not on the list")



# Ternary operator (one-line if-else)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")


# compering string

password= "secret123"
if password == "secret123":
    print("Access granted")
else: 
    print("No access!")

# Chaining comparisons
x =15
if 10 < x < 20:
    print("x is between 10 and 20")

#truthy or falsy
user_input = ""
if user_input:
    print("input provided.")
else: 
    print("no input provided")