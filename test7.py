# Program make a simple calculator
# This function adds two numbers

#https://www.programiz.com/python-programming

def add(x, y):
	return x + y

def subtract(x,y):
	return x -y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

print("choose function.")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice=input("Enter choice(1/2/3/4): ")
print("choice = ", choice)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
	print("Choice is 1")
	print(num1,"+",num2,"=", add(num1,num2))
elif choice == 2:
	print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == 3:
	print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == 4:
	print(num1,"/",num2,"=", divide(num1,num2))
else:
	print("Invalid input")
	print("Valid inputs are 1/2/3/4)
	print("option are add/modify/delete")
