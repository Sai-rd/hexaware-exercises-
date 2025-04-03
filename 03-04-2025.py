'''Task 1'''

'''1) Write a Python program that takes an integer input from the user and prints "Positive" if the number is greater than 0.'''
a=int(input("Enter a number : "))
if(a>0):
    print("positive")

'''2)Given a variable temperature, write an if statement that prints "Hot day!" if temperature is greater than 30.'''
temp=int(input("Enter temperature : "))
if(temp>30):
    print("Hot day!")

'''3) Write a program that asks the user to enter a number and checks if it is even. If it is, print "Even number".'''
b=int(input("Enter a number : "))
if(b%2==0):
    print("Even number")

'''4) Write a Python program that checks if a number is even or odd. Print "Even" if it is even, otherwise print "Odd".'''
c=int(input("Enter a number : "))
if(c%2==0):
    print("Even ")
else:
    print("Odd")


'''5)Write a program that asks the user to enter their age. If they are 18 or older, print "Eligible to vote", otherwise print "Not eligible to vote".'''
age=int(input("Enter a age: "))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")

'''6)Create a program that asks the user to enter a password. If the password is "admin123", print "Access Granted", otherwise print "Access Denied".'''
password=input("Enter the password: ")
if(password=='admin123'):
    print("Access Granted")

else:
    print("Access Denied")

'''7)Write a program that takes a number as input and prints:
 
"Positive" if the number is greater than 0,
 
"Negative" if it is less than 0,
 
"Zero" if it is exactly 0'''

d=int(input("Enter a number : "))
if(d>0):
    print("Positive")
elif(d<0):
    print("Negative")
else:
    print("Zero")

'''8)Create a grading system where a user enters a score (0-100). The program should print:
 
"A" if the score is 90 or above,
 
"B" if the score is between 80 and 89,
 
"C" if the score is between 70 and 79,
 
"D" if the score is between 60 and 69,
 
"F" if the score is below 60.'''

marks=int(input("Enter the marks : "))
if(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
else:
    print("F")

'''9)Write a Python program that checks if a given year is a leap year. A leap year:
 
Is divisible by 400, or
 
Is divisible by 4 but not by 100.'''

yr=int(input("Enter the year : "))
if(yr%400 or yr%4) and yr%100!=0:
    print("Leap Year")
else:
    print("Not a leap year")

'''10)Write a Python program that takes the current time (in 24-hour format) as input and prints:
 
"Good Morning" if the time is between 5 and 12,
 
"Good Afternoon" if the time is between 12 and 17,
 
"Good Evening" if the time is between 17 and 21,
 
"Good Night" otherwise.'''

tme=int(input("Enter the time in 24hr format : "))
if(tme>=5 and tme<12):
    print("Good Morning")

elif(tme>=12 and tme<17):
    print("Good Afternoon")

elif(tme>=17 and tme<21):
    print("Good Evening")

else:
    print("Good Night")




'''Task 2'''

'''Pattern 1'''
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

'''Pattern 2'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''Pattern 3'''
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

'''Pattern 4'''
size = 5  

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''Pattern 5'''

size = 7  

for i in range(size):
    for j in range(size):
        if (i == 0 or i == size - 1) and j > 0: 
            print("*", end=" ")
        elif j == 0:  
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


'''Task 3'''


'''1) Reverse a list in Python'''
li=[1,2,3,4,5]
li=li[::-1]
print(li)

'''2) Concatenate two lists index-wise'''
a=[1,2,3,4,5]
b=[2,3,4,5,6]
result=[a[i]+b[i] for i in range(len(a))]
print(result)

'''3) Turn every item of a list into its square'''
a=[1,2,3,4,5]
res=[i*i for i in a]
print(res)

'''4) Concatenate two lists in the following order'''
a=[1,2,3,4,5]
b=[2,3,4,5,6]
res=a+b
print(res)

'''5) Iterate both lists simultaneously'''
a=[1,2,3]
b=[4,5,6]
for i in range(len(a)):
    print(a[i],b[i])

'''6) Remove empty strings from the list of strings'''
a=['abc',' ','bcd']
for i in a:
    if i==' ':
        a.remove(i)
print(a)

'''7) Exercise 7: Add new item to list after a specified item'''
a=[1,2,4,5]
b=7
a.append(b)
print(a)

'''8) Extend nested list by adding the sublist'''
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)

'''9)Replace lists item with new value if found'''
a=[1,3,4,5,6]
for i in range(len(a)):
    if(a[i]==5):
        a[i]=8
print(a)

'''10) Remove all occurrences of a specific item from a list.'''
a=[2,1,2,1,3,4,2,5]
for i in range(len(a)):
    if(a[i]==2):
        a.remove(a[i])
print(a)
