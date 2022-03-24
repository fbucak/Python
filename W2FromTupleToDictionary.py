# Write a Python program that returns a dictionary which consists the unique elements in the following tuple
# as keys and the number of occurrences of elements as values.
# tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)

tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)
numbersList=list(tuple1)
numberDict={}
for i in range(len(numbersList)):
    count=numbersList.count(numbersList[i])
    numberDict.update({numbersList[i]:count})
print(numberDict)