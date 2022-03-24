x=int(input("Please enter a number"))
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(x):
    numbers.append(numbers[0])
    numbers.pop(0)

print(numbers)

