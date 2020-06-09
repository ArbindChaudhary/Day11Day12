#1.Create three variables in a single a line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string

a,b,c=2, 3.5,'Arbind'
print(type(a))
print(type(b))
print(type(c))


#2.Create a variable of value type complex and swap it with another variable whose value is an integer.

x =2
y =2+3j
x,y =y,x
print("value of x:", x)
print("value of y:", y)

#3.Swap two numbers using the third variable as the result name and do the same task without using any third variable.

numx=1
numy=3
temp=numx
numx=numy
numy=temp
print("value of numx:", numx)
print("value of numy:", numy)

#4. Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version

num=int(input("Enter a number:"))
print("You Entered the number:", num)

#5. Write a program to complete the task given below:
#Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
#Use z for adding 30 into it and print the final result by using variable result.

num1=int(input("Enter 1st number between 1-10:"))
num2=int(input("Enter 2nd number between 1-10:"))
z=num1+num2
result = z+30
print("Your sum is :", z)
print("You final result is:", result)


#6. Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc

d=eval(input("enter the value:"))
print("the input value data type is :", (type(d)))

#7. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
# Answer: It's not going to change the value because a variable can only have one data type


