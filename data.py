# WEEKEND ACTIVITY ON DATA STRUCTURES

# 1.	Create a list of the 10 elements of four different types of Data Types like int, string, complex and float.

List=[1,  1+2j, "Arbind Chaudhary", 3.4, 2.5, 5, "BootCamp", 2+2j, 66.7, 88]
print(List)


# 2. 	Create a list of size 5 and execute the slicing structure 

x=[1,2,3,4,5]
y=x
print(x[0:3])
print(x[2:])
print(x[-2:])
print(x[::2])
print(x[1:4:2])
print(x[::-1]) 


# 3. 	Create a list of given structure and run 
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
y=slice(0,9,2)
print(x[y])
print(x[::-1])
print(x[5][5][0])


# 4. 	Create a list of thousand number using range and xrange and see the difference between each other.

# initializing with range() 
a = range(1,10000) 

# initializing with xrange() 
x = xrange(1,10000) 

# testing the type of a 
print ("The return type of range() is : ") 
print (type(a)) 


# testing the type of x 
print ("The return type of xrange() is : ") 
print (type(x)) 


# 5. 	How Tuple is beneficial as compare to the list?

#Answer=>   tuple cannot be changed once it is created where as we can change the list after it's created also Tuples are faster than list


# 6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

list=range(1,101)
def func(list1):
    for i in list1:
        if (i%3==0 or i%2==0):
            print (i)
func(list)


# 7. 	Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.


string = input("Enter your string")

newstr = string;

vowels = ('a', 'e', 'i', 'o', 'u');
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"");
print(newstr)




# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

string1="hello my name is abcde"
string1=string1.split()
for i in string1:
    if (len(i)%2==0):
        print (i)


# 9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

def printPairs(arr, arr_size, sum):
     # Creating an empty hash set 
    s = set() 
      
    for i in range(0, arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            print ("Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")"
        s.add(arr[i])
  
    # driver program to check the above function 
x = [1,2,3,4,5,6,7,8,9,-1] 
n = 8
printPairs(A, len(x), n) 


# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)
print("Sum of Even number in the  List is",sum(even))
print("Sum of odd numbers in the List is",sum(odd))


# 11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  
#                       Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('My name is patel ronak where patel is last name & ronak is first name '))



# 12.          Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

x=(1,2,3,4,5,6,7,8,9,10)
list=[]
for i in x:
    if i%2==0:
        list.append(i)
y=tuple(list)
print(y)
print(type(y))
