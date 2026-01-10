letters = ["a", "b", "c", "d", "e"]
letters[0] = "A"
print(letters[0:3])
print(letters[::2])

numbers = list(range(20))
print(numbers)
print(numbers[::-1])


numberTwo = [1,2,3,4,4,4,4]
first,second, *others = numberTwo
print(first)

first = numberTwo[0]
second = numberTwo[1]
others = numberTwo[2:]
print(first)
print(second)
print(others)


lettersTwo = ["a", "b", "c", "d", "e"]
items = (0, "a")
for index, letter in enumerate(lettersTwo):
    print(index, letter)

lettersThree = ["a", "b", "c", "d", "e"]
items = (0, "a")
index, letter = items
for letter in enumerate(lettersThree):
    print(index, letter)


lettersFour = ["a", "b", "c", "d", "e"]

# Add
letters.append("f")
letters.insert(0, "A")


# Remove
letters.pop(0) #removes last item
letters.remove("b")
del letters[0:2]
print(letters)

