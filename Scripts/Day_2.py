#June 21,2021
#Beginner's Workshop on Python
#US EMBASSY - DHAKA
#Script : Akif Islam


#Offtopic
numbers = input().split()
print(numbers)


#1. String Functions / Methods | Example 01

#What is a Function?
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alphabets))
print(alphabets[5]) #F
print(alphabets[0:5]) #ABCDE
print(alphabets[0:-1]) #ABCDEFGHIJKLMNOPQRSTUVWXY
print(alphabets[3:4]) #D
print(alphabets[3:3]) # Print Nothing
print(alphabets[0:4]) # Print 1 theke 4 no letter. 0 4
print(alphabets[5:10]) #print 5 theke 10


# #Offtopic
print(alphabets[::-1]) #Reverse a String

#2. String Functions | Example 2
course = "Beginner's Course on Python"
print(len(course))
print(course[0]) # B
print(course[5]) #n
print(course[7]) # r
print(course[8]) # ' (apostrophy)
print(course[10]) # (Space)
print(course[-6:]) #Python
print(course) #purata Print
print(course[0:]) #purata


#3. String Functions | Example 3

ABString = "ABC def GHI jkl"
print(ABString.title())
print(ABString.lower())
print(ABString.upper())
print(ABString.find('a'))  #Return index of first occurance of a  #-1


#4. String Functions | Example 4

words = "AABBABABABAAAA"
print(words)
print(words.count('A'))
print(words.__contains__("BABA"))
print("BABA" in words)
print(words.count('X')) # 0
print(words.find('X')) # -1
print(words.replace("A","X")) #XXBBXX...
print(len(words)) #14
print(words.center(30)) #Weird Function


# Python strings are immutable (i.e. they can't be modified).

# Class Task : Replace First Character
S = "XXBBCCXDD"
print(S.replace(S[0],"*"))

# 5. Arithmatic Operations

x= 10
y= 6
print(x+y)
print(x/y)
print(x//y) # #integer divison

# #Example of Lift :Suppose a lift can take 100 KG. 2 Person enters : 70KG & 40KG
# How many persons we can take?? #Answer is 1


print(10%8) #Reminder / VagShesh
print(10*2)
# print(123456789101112131415**7654)


# End ....... # Return 0