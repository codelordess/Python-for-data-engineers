point = (1,2,3)
print("Before swap:", point)
x,y,z = point
if 10 in point:
    print("10 is in the tuple")

# This line has a syntax error; it should be print(point[0])
# print [0] = 10


# Swap values
x = 10
y = 11

x,y = y,x


print("After swap: x =", x, "y =", y)
print("After swap:", point)


#typed array
from array import array

numbers = array('i', [1,2,3,4,5])
#numbers[0] = 1.0

numbers = [1,1,2,3,4,5]
first = set(numbers)
second = {3,4,5,6,7}
print(first | second)
print(first & second)
print(first - second)




