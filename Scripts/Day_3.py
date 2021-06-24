#June 22,2021
#Beginner's Workshop on Python
#US EMBASSY - DHAKA
#Script : Akif Islam

# 1. Math Functions
import math
A = 150.252
print(A)
print(math.ceil(A))
print(math.floor(A))
print(math.factorial(5))
print(round(A))
print(math.gcd(12,16))
print(round(4.51)) #4.50 --> 4 Dhorbe, #4.51 hole ---> 5 Dhorbe


# 2. Assigning from Right to Left
A = 50
B = 10
A = A + A + B
print(A) #110   #ASK QUESTION


# Example
C = 0
A = 10
A = A + 20

B = A
B = C
print(C) #0 #ASK QUESTION




#3. IF ELSE (1):
A = 5
B = 10
C = 50

if(A>10 and B<20):
    print("OK")


#4. IF ELSE (2):
number = 100

if(number > 5):
    print("Greater than 5")
else :
    print("Smaller than 5")



# 5. IF ELSE (3):
name = input("What's your name?")
if(name == "ABUL") :
    print("You are Abul")
else:
    print("NO!")




# 6. IF ELSE (4):
password = input("What's your name?")
length_of_password = len(password)

if(length_of_password<4):
    print("Your password is too short !")
elif (length_of_password>20):
    print("Too long password :( !")
else :
    print("Alright !")



#7. IF ELSE (5) | CLASS TASK
amount = int(input("Enter amount to convert : ")) #100
query = input("Is it TK or $ ?") #$

if(query=="$"):
    print(f"{amount*80} TK")
else:
    print(f"{amount/80} $")



# 8. IF ELSE (6) | CLASS TASK :
amount = input("Enter amount to convert : ") #100

if amount.endswith("$"):
    value = amount.replace("$"," ")
    value = int(value.strip())

else:
    value = amount.replace("TK"," ")
    value = int(value.strip())

# print(value)

if amount.endswith("$"):
    print(f"{value*80} TK")
else:
    print(f"{value/80} $")



#....End....