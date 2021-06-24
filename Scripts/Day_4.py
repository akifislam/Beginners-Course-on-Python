#June 23,2021
#Beginner's Workshop on Python
#US EMBASSY - DHAKA
#Script : Akif Islam


# 1. String Strip ()
words = "Akif"
print(words.strip()) #Space Removed
print(words.strip("k")) #Nothing Removed
print(words.strip("f")) #Aki
print(words.strip("Ak")) #if

#2. String Strip() (2)

text = "!!!!hello!!!!"
print(text.strip('!')) #hello
#Strip functions only remove from left side and right side.

text2 = "aaaaahelloaaaahelloaaaaaaaa"
print(text2.strip('a'))

print(text2.lstrip('a'))
print(text2.rstrip('a'))


#3. Printing 1 to 10 with While Loop
i = 1
while(i<=10):
    print(i,end=" ")
    i+=1

#4. Printing 1 to 100 with While Loop

i = 1
while(i<=100):
    print(i,end=" ")
    i+=1

#5. How to print Hello World 5 times?
i = 0
while(i<5):
   print("Hello World\n")
   i+=1

#6. How to print Hello World for Infinity Times without increment?
i = 0
while(i<5):
   print("Hello World\n")


#7. How to print Hello World for Infinity Times (while (True))?

while(True):
   print("Hello World\n")


#8. How to print all odd numbers from 1 to 50?

i = 1
while(i<50):
   print(i,end=" ")
   i+=2

print()

#9. How to print all even numbers from 1 to 50?

i = 2
while(i<=50):
   print(i,end=" ")
   i+=2


#10. How to use break  in loop?
i = 0
while(i<100):
    i=i+1
    print("Hello")
    if(i == 4):
        break

# 11. How to use continue in loop?
i = 0
while(i<6):
    i=i+1
    if(i == 4):
        continue # 4 Skipped
    print(i)




# 12. Generating Random Number | Guessing Game

import random
i = 0

while(i<10):
    secret_number = random.randint(1,10) #?
    # it is inclusive or exclusive? Check Docu. (Ans : inclusive)
    i = i +1
    #i+=1
    print(secret_number,end=" ")


# 13. Both are same
i= i +1,
i+=1 same



#14. Making Guessing Game

import random
no_of_chances = 5
secret_number = random.randint(1,10)

while(no_of_chances>0):
    no_of_chances = no_of_chances -1
    user_input = int(input("Enter your guess : "))
    print(f"Chances Left : {no_of_chances}")


    if(user_input>secret_number):
        print("Guess something lower !")
    elif (user_input<secret_number):
        print("Guess something higher")
    else:
        print("Congratulations !")
        break

if(no_of_chances==0):
    print("Game Over !")




#15. for loop in String (A):
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in A:
    print(i,end="-")




# 16. It will print 0 to 6
for x in range(6):
  print(x)



# 17. It will print 2 to 6
for x in range(2, 6):
  print(x)



#18.  It will print 2,4,6,8,10,12.....
for x in range(2, 30,2):
  print(x,end=" ")



# 19. Print 10 to 0
for i in range(10, -1, -1):
    print(i)




#20  It will print 1,3,5,7,9.....

for x in range(1, 30,2):
  print(x,end=" ")



# 21.  (0 to 5)
for x in range(6):
  print(x)

# 22. 30, 28, 26, 24, 22, 20 ....
for x in range(30, 2,-2):
  print(x,end=" ")


#23. Def - Function

def my_function():


# 24. Default Value Pass
def my_function(country = "Norway"):
  print("I am from " + country)


# Star Printing
n = int(input("Size of Star : \n"))
for i in range (0,n):
    for j in range (0,i+1):
        print("*",end="")
    print()






def sum(a=10,b=10):
    return a+b


def Sayhi()


