"""
Omar Rizk
CS 100 2021S Section 108
HW 07 March 12, 2021
"""
import string
def lilCricFriend(wordList, text):
#Problem 1
    l = theBells.lower()
#Problem 2
    l = theBells.replace('--', ' ')
#Problem 3
    l = theBells.split()
#Probem 4
    w = []
    for i in l:
        w.append(i.strip(string.punctuation))


#Problem 5
    count = 0
    for i in wordList:
        for s in w:
            if i.lower() == s:
                count += 1
            
#Problem 6
    ratio = 0
    wordCount = len(theBells)
    ratio = count/wordCount
    return ratio

#Problem 7
    print('bellsAAnFrequency', litCricFriend(['a', 'an'], theBells))
    print('Canto XII Frequency',litCricFriend(['a', 'an'], Canto XII))
    print('bellsAAnFrequency',litCricFriend(['the'], theBells))
    print('Canto XII Frequency', litCricFriend(['the'], Canto XII))

#Problem 8
    '''
    The results are different for 'a', and 'an', as well as for 'the'
    '''

    
    







