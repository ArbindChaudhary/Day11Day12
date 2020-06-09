#1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

List=[1, "arbind", 2+3j, 2.5, 3,"python", 4+6j, 5.6, 7, "training"]
print(List)

#2. 	Create a list of size 5 and execute the slicing structure 

num = [10, 20, 30, 40, 50]
print(num[1:3])
print(num[0:4])


#3. Write a program to get the sum and multiply of all the items in a given list.


import math 
list = [1, 2, 3]   
result = math.prod(list) 
 
print("Product of all element in given list:",result) 


 
list1 = [1, 2, 3, 4, 5] 
total1 = sum(list1) 
print("Sum of all elements in given list: ", total1) 



#4.   	Find the largest and smallest number from a given list.
list=[1,2,3,4,5,6,7]

print ("Largest number in the list of element is =",max(list))
print ("Smallest number in the list of element is=",min(list))

#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 

list = [11,22,33,44,55,66,77,88]
print ("list you provided is:", list)

for i in list:
    if (i%2==0):
        list.remove(i)
        print("list after removing evn numbers:",list)


#6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def squarelist():
    list=[]
    for i in range(1,31):
        list.append(i**2)
    
    return list[:5],list[-5:]

first,last=squarelist()
print ("Square of first 5 element is :",first)
print ("Square of Last 5 element is :",last)

#7.	Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
print("the current list is:",list1)
list1[-1:] = list2
print("list after replacing last element is:",list1)


#8.	Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
c={}
for d in (a,b):c.update(d)
print(c)

#9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

n=int(input("enter the nth number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 



#10. 	Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#The output should be:
#[‘34’,’67’,’55’,’33’,’12’,’98’]
#(‘34’,’67’,’55’,’33’,’12’,’98’)

values = input("Enter the elements : ")
list = values.split(",")
tuple = tuple(list)
print('The List is : ',list)
print('The Tuple is : ',tuple)
