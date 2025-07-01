# For loop

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nReversed counting from 5 to 1:")
for i in range(5, 0, -1):
    print(i)


# While loop
count = 1
print("while loop")
while count <= 5:
    print(count)
    count += 1


# Reversed While loop
count = 5
print("\nReversed while loop")
while count >= 1:
    print(count)
    count -= 1

# Looping thru a list

fruits = ["apple", "banana", "cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)

# Reversing a list
print("\nMy Reversed list")

for fruit in reversed(fruits):
    print(fruit)


# Loop with enumerate
print("fruit with indices")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")


# loop with Dictionaries
person = {"name":"john","age":30,"city":"NYC"}
print("\nPerson dict")
for key,value in person.items():
    print(f"{key}:{value}")

# List comprehension (compact loop for creating lists)
# squares = [for x in range(1,6)]