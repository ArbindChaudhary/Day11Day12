# 1. 	Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

x="1234abcd" [::-1]
print(x)



# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def function(x):
    y={"upper case":0, "lower case":0}
    for c in x:
        if c.isupper():
           y["upper case"]+=1
        elif c.islower():
           y["lower case"]+=1
        else:
           pass
    print ("Original String : ", x)
    print ("Total no. of Upper case characters : ", y["upper case"])
    print ("Total no. of Lower case Characters : ", y["lower case"])

function("Consulatdd is doing Great Work")


# 3.        Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,2,3,3,4,55,6,77,85,333,444,333,444,44,8,8,8,8,11,1,11,85])) 


# 4.         Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

user=input("Enter the string seprated by hypen\t:")

word=[i for i in user.split("-")]
word.sort()
print("-".join(word))


# 5.         Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def uppermethod(user):
    x=user.upper()
    print(x)
user=input("Please type a sentence : ")
uppermethod(user)


# 6.          Define a function that can receive two integral numbers in string form and compute their sum and print it in console.


def calculateSum (x,y):
	s = int(x) + int(y)
	return s 


                   # take two integral numbers as strings
num1 = "10"
num2 = "20"

                    # calculate sum
sum = calculateSum (num1, num2)

                    # print sum
print ("Sum = ", sum)


# 7.        Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.


def length_of_string(str1, str2):
	if (len(str1) == len(str2)):
		print(str1)
		#print("\n")
		print(str2)

	elif (len(str1) < len(str2)):
		print(str2)
	
	else:
		print(str1)

stri1 = input(str("Enter the First String: "))
stri2 = input(str("Enter the Second String: "))

print("\n")

length_of_string(stri1, stri2)



# 8.        Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.


def printValues():
	l = list()
	for i in range(1,21)
		l.append(i**2)
	print(l)
		
printValues():


# 9.         Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def numbers(limit):
        count_odd = 0   
        count_even = 0
        for x in range(0,limit+1):
                if not x % 2:
                        count_even+=1
                        print(x, " is even")
                else:
                        count_odd+=1
                        print(x," is odd")
        
        print("Number of even numbers are :",count_even)
        print("Number of odd numbers are :",count_odd)
print("Enter a limit: ")
l=int(input())
numbers(l)



# 10. 	Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

list = [1,2,3,4,5.6,7,8,9,10] 
output = [] 
for num in list:
    if num % 2 == 0:
        output.append(num) 

print(output) 


# 11. 	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions

intList = [1,2,3,4,5,6,7,8,9,10]
 
intSqr = map(lambda x: x**2,filter(lambda   x: x%2==0, intList))
 
print(list(intSqr)) 


# 12. 	Write a function to compute 5/0 and use try/except to catch the exceptions

def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError:
    print ("Can not divide by zero  ")


# 13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 

import operator     
from functools import reduce    
list = [[1, 2, 3], [4, 5], [6, 7, 8]]  
joinlist = reduce(operator.add, list)  
print(joinlist)                        
str1=""
for i in joinlist:
    str1+=str(i)
print (int(str1))



#  14. 		
# (i) def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)


