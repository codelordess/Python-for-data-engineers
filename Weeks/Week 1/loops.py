#for loop

for number in range (1, 10, 2):
    print ("Attempt", number, number * ".")

count = 0
for number in range (1, 10):
    if number % 2 == 0:
        count += 1
        print (number)
#formatting a string
print(f"We have {count} even numbers ")

sucessful = False
for number in range(3):
    print("Attempt")
    if sucessful:
        print("Successful")
        break
    else:
        print("Attempted 3 times and failed")


#Nested for loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


#Type in python

print(type(5))
print(type(range(5)))

#iterable string
for x in "PYTHON":
    print(x)

#iterable list
for x in [1,2,3,4]:
    print(x)

#iterable custom object. we define this object at the point of calling the class
shopping_cart = ""
for item in shopping_cart:
    print(item)

command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)




