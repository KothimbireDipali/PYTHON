#Excercise
'''
1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to number second number'''

num1= int(input("first input number :::: "))
print(" The value is " , num1)
num2= int(input("second input number :::: "))
print(" The value  is " , num2)
#a) addition 
print(" The Addition  is " , num1+num2)

#b) first number squared 2 
print("square:",num1**2)



#c) first number raised to number second number
result=pow(num1,num2)
print("first num raised to second num:",result)


#2) Accept String from user and output upper case of the input string 
Str=(input("enter the string :::: "))
print("Upper case of the string is", Str.upper())

#3) Define a variable named "raise_salary_percentage" and get the salary raise 
#percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console

name="poonam"
existing_salary=900
raise_salary_percentage=float(input("raise_salary_percentage :::: "))
inc_sal=(existing_salary*(raise_salary_percentage/100))
sal=existing_salary+inc_sal
print("Incremented salary is :",sal)

# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches

height= float(input("Enter the height in cms :::: "))
print("Height in inches:",(height/2.54),"inch") 
print("Height in foot/feet:",round((height/30.48),2),"foot") 


# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees
dollar= int(input("Enter the dollars:::: "))

print("No of Dollers is",dollar*82,"Rupees")

# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"

source=str(input("ENter the source: "))
destination=str(input("Enter the destination: "))
fare=float(input("Enter the fare amount in INR: "))
discount=float(input("Enter the discount: "))
print("Fare from ", source,"to",destination,"is",fare-((fare*discount)/100),"INR with has a discount of ",discount,"%")
