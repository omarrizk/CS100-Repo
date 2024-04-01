"""
Omar Rizk
CS 100 2021S Section 108
HW 01 January 29, 2021
"""

#b
minutes = 1
seconds = 60
hours = 0

#c
days = 1.5
weeks = 14.3221
feet = 4.81

#d
favoriteMovie = "lion king"
bestSubject = "math"
topSchool = "NJIT"

#1.1
#1) you get a syntax error
#2) you will another syntax error
#3) putting a plus sign before a number will add its value and 2++2 would give you 4
#4) you will get an error because it is an invalid token
#5) you will get an invalid syntax error

#1.2
seconds = (42*60) + 42
print(seconds)

miles = 10 * 1/1.61
print(miles)

paceSeconds = int(seconds // miles)
paceMinutes = int(paceSeconds // 60)
paceSecondsTwo = paceSeconds - (paceMinutes * 60)
print(paceSecondsTwo)

timeHours = ((seconds/60)/60)
avgSpeed = miles/timeHours
print(avgSpeed)

#2.1
# 42 = n is not legal
# x=y=1 is legal
# You won't get any errors
# You will get and invalid syntax error
# You will get a name error

#2.2
volume = (((4/3) * 3.14) * (5**3))
print(volume)

coverCost = 24.95
bookstoreDiscount = (24.95 * .4)
bookstorePrice = 60 * (24.95 - bookstoreDiscount)
shipping = 3 + (.75 * 59)
totalPrice = (bookstorePrice + shipping)
print(totalPrice)

