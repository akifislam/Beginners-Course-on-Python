#June 20,2021
#Beginner's Workshop on Python
#US EMBASSY - DHAKA
#Script : Akif Islam


# 1. Printing Hello World

print('Hello World')
print('Hello Akif !')


# 2. How Python Code Executed? # Interpreter
print("A")
print("B")
print("C")
print("D")
print("E")
print()

# 3. Print something with 's
# Wrong : print('Beginner's Course in Python')
print("Beginner's Course in Python")
print('Akif says : "Do not work. Just Eat & Sleep"')
print('''Akif says : "Don't not work. Just Eat & Sleep"''')


# 4. Question :
# ভাই এগুলো প্রিন্ট করার কি আছে? এগুলো তো মাইক্রোসফট ওয়ার্ডেরি লেখা যায়
# Dyanmically Letter Send


# 5. Keeping in a variable and print
myname = "Akif" #String Type

print("Hi ",myname)
print(f"Hi {myname}") #Formatted String

print(f'''
Hi !
This is {myname}
Welcome to Beginner's Workshop in Python
''')


#6. Taking Input and print "Hi + {name}"
new_name = input("What is your name? | Expected String ")
print(f" Hi {new_name}")


# 7. Class Task
# Print "Akif's Favourite Colour is Red"
new_name = input("What is your name? | Expected String ")
fav_colour = input("What is your favourite colour?")
print(f"{new_name}'s favourite colour is {fav_colour}")


#Break.......

# 8. Variable Explained !
# Definitions : Temporarilty Stores data in computer memory

#Previously,
myname = "John" (String)
price = 10
Temperature = 98.2
isGood = True

price = 10 # Box titled 'price'
price = 20
print('price') #cannot do anything
print(price)
price = price + 20 #Can Increase
print(price)
print("Current Price is : ", price)



# Different Data Types
rating = 4.9 #Floating Point Numbers
name = "Mosh" #String Varible
isGood = True #Boolean


#9. Interger and String Problem | Type Conversion

#Wrong | No Type Conversion
birth_year = (input('Birth Year : '))
age = 2021 - (birth_year)
print(age)

#Type Conversion
birth_year = int(input('Birth Year : '))
age = 2021 - (birth_year)
print(age)

#10. Class Task
# Show Slide :
# Print Sum of 2 Numbers

# Day 1 Time Exceed
# ----- End-------