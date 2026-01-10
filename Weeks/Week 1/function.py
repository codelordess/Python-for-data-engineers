def greet():
    print("Hi there")
    print("Welcome aboard")
greet()



def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Hephzibah", "Emereole")

def greet (name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)
print (f"Contents have been written to a file {message}")


def increment(number, by):
    return number + by

def greet(name):
    print(f"Hi {name}")

print(greet("Mosh"))


print(increment (2, 1))
print(increment (number=2, by=1))

#this takes only the specified parameter
def multiply(x, y):
    return x * y

multiply (2,5)

#taking multiple arguments in the function call
def multiplyTwo(*numbers):
    for number in numbers:
        print(numbers)

multiplyTwo(2,3,4,5)


#Sample of a dictionary
def save_user(**user):
    print(user["name"])

save_user(id=1, name="John", age=22)

