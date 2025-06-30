# name = input("What is your name? ")
# print("hello", name)

# age = int(input("how old are you? "))
# years_to_100 = 100 - age
# print(f"You will be 100 in {years_to_100} years")


# num1 = float(input("Enter your number "))
# num2 = float(input("Enter your number "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}")


# Working with multiple input on one line
# x, y = input("enter two values separated by space: ").split()
# print(f"first value: {x}, second value: {y} ")

user_choice = input("Choose a color (or press enter for default): ")
if user_choice == "":
    user_choice = "blue"
print(f"Select color: {user_choice}")


#possibilities are endless
length = float(input("Enter length in meters: "))
print(f"That's {length * 100} centimeters")

