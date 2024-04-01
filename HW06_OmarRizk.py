"""
Omar Rizk
CS 100 2021S Section 108
HW 06 February 26, 2021
"""

def hasFinalLetter(strList, letters):
    finalList = []
    for string in strList:
        if string[-1] in letters:
            finalList.append(string)
    return finalList

stringOfValues = 'HiLoWplt'
test1 = ['test', 'python']
test2 = ['hello', 'school', 'ray']
test3 = ['return']
print(hasFinalLetter(test1, stringOfValues))
print(hasFinalLetter(test2, stringOfValues))
print(hasFinalLetter(test3, stringOfValues))

def isDivisible(maxInt, twoInts):
    finalList = []
    for i in range(1,maxInt):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            finalList.append(i)
    return finalList
twoInts = (3,4)
maxInt = 48
print(isDivisible(maxInt, twoInts))
twoInts = (5,6)
maxInt = 31
print(isDivisible(maxInt, twoInts))
twoInts = (5,2)
maxInt = 1
print(isDivisible(maxInt, twoInts))

