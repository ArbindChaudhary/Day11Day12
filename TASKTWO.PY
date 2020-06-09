# 1. 	Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “c” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string

num =int (input("Enter a number: "))
if num %3 == 0 and num %5 == 0:
   print("Consultadd Python Training")
elif num %3 ==0:
   print("Consultadd")
elif num %5 == 0:
   print("c")

else:
   print("bye bye ")
   


# 2. Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition 
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If USer Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
#Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
#At the end if the answer of any operation is Negative print a statement saying “zsa”
#NOTE: At a time user can perform one action at a time.





print("Choose what operation you want to perform.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Average")

while True:
   
    choice = input("Enter your choice(1,2,3,4,or5): ")

    
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print( "the sum is :", num1 + num2)

        elif choice == '2':
             print( "the difference is :", num1 - num2)

        elif choice == '3':
            print( "the product is :", num1 * num2)

        elif choice == '4':
            print( "the answer is :", num1 / num2)
           
            
        elif choice == '5':
                print ("Enter 2 more numbers")
                number1= float(input("Enter first number:"))
                number2=float(input("Enter second number:"))
                sum= num1+num2+number1+number2
                average =sum/4
                print("Average is:", average)
                
                
        break
   
        
    else:
        print("Invalid Input")



#3. 	Write a program in Python to implement the given flowchart:


#5.Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


#4. 	Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”


while(True):
    number=int(input("Enter a positive number :"))
    if(number<0):
        print("It's Over")
        break
    elif(number>0):
        print("Good Going")
        continue



#6. What is the output of the following code examples?
#  x=123 
#  	   for i in x:
# 	print(i)

# Answer: This will give an error message


# i = 0
# while i < 5:
#    print(i)
#     i += 1
#     if i == 3:
#        break
# else:
# print(“error”)

# Answer: The out put will be 0,1,2

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
#Answer: The output will be 0,1,2,3,4


#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
 #      Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

for n in range(6):
    if (n==3 or n==6):
        continue
    print(n)



# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#     Expected output: consul12
#    Letters 6
#   Digits 2

s = input("Enter a string:")
digit=0
letter=0
for c in s:
    if c.isdigit():
        digit=digit+1
    elif c.isalpha():
        letter=letter+1
    else:
        pass
print("Letters:", letter)
print("Digits:", digit)


# 9. Read the two parts of the question below: 
# Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
#Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

luckynumber=7
while (True):
    z= int(input("Guess the lucky number:"))
    if (z==luckynumber):
        break



#modified version

luckynumber=7
while (True):
    answer=input("Do you want to continue guessing:")
    if (answer=="no"):
        break
    else:
        number=int(input("Guess the lucky number:"))
        if (number==luckynumber):
            break
    


#10 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
   #        		counter=1
	#	While counter <= 5:
	#		print(“Type in the”, counter, “number”
	#		counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.

   counter = 1
      while counter <= 5:
        number = input("Guess the " + str(counter) + ". number ")
        if number != 5:
          print "Try again."
        else:
          print "Good guess!"
        counter = counter +1
      else:
        print "Game over"

#11 In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful” 

 while counter <= 5:
        number = input("Guess the " + str(counter) + ". number ")
        if number != 5:
          print "Try again."
        else:
          print "Good guess!"
          break
        counter = counter +1
      else:
        print "Sorry but that was not very successful"



