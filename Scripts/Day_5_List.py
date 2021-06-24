#June 24,2021
#Beginner's Workshop on Python
#US EMBASSY - DHAKA
#Script : Akif Islam

import math

# 1. Star Printing
n = int(input("Size of Star : \n"))

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()


for i in range(n-2, -1,-1):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()



#2. List

# Making a List
grocery_list = ["rice","potato","tomato","Ginger","Chili"]
print(grocery_list)
print(grocery_list[0:2])

#Insert a new item
grocery_list.append("water")
print(grocery_list)

# List Declare list ()
l2 = list()
print(l2)

l2.append(4)
print(l2)

l2.append("computer")
print(l2)

l2.append(True)
print(l2)

# What is the n-th index?

second_item = grocery_list[1] #Potato
print(second_item)

#What is the lastth index?
print(grocery_list[-1])

#List Sort ()
numbers = [55,51,50,45,25,12,22,11,2,5,6]
numbers.sort()
print(numbers) #Sorted

#How to save sorted in other variable?
numbers = [5,4,2,1,9,22]
sorted_list = sorted(numbers)
print(sorted_list)
print(numbers)

# Star Print Again with List | Mosh
serial = [1,2,3,4,5,4,3,2,1]

for i in serial:
    print('*' * i)

#Write a program to find the largest number in a list
num = [1,5,2,4,9,2,10,42,11,555,2,1000,-5]

# largest_number = -math.inf
largest_number = num[0]

for number in num:
    if(number>largest_number):
        largest_number = number

print(largest_number)


# Same program using sort
print("-----\n\n\n")

sorted_num = num
sorted_num.sort()
print("Using Sort Func : ",sorted_num[-1])
sorted_num.sort(reverse=True)
print(sorted_num)

# Remove
print(sorted_num.count(2))
sorted_num.remove(2)




