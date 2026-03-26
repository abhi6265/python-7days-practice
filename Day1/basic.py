#first code in python
print("Hello World")
#print() gives output to the screen
print("welcome to python programming")

#variables in python
#variable is a name that refers to a value stored in memory
#variable is uselly used to store data
#variable==> container that holds a value
#variable name should be meaningful and should not start with number
integer=10
string="Python programing"
Float_number=3.14
Bool_value=True

#python non required no variable type decleration

#type() function is used to check the data type of a variable
print(type(integer))
print(type(string))
print("String is:",string)
print("integer is:",integer)
print("Float number is:",Float_number)
print("Boolean value is:",Bool_value)
#python is case sensitive language
#same variable name with different case is treated as different variable
name="John"
print(name)
name="deon"
print(name)


#f-String (Modern Way – Important)
name="Abhi"
age=25
print(f"my name is {name} and i am {age} years old")


#input() function is used to take input from the user
name=input("Enter your name: ")
age=input("Enter your age: ")
print(type(age))
#inputr() function always returns a string, so we need to convert it to the desired data type
age=int(input("Enter your age: "))
print(f"my name is {name} and i am {age+5} years old")

#basic arithmetic operations

a=10
b=5
print("addition",a+b)
print("Substraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Floor Division",a//b)
#question: what is the difference between division and floor division
#division gives the result in float and floor division gives the result in integer

print("Modulus",a%b)
print("Exponentiation",a**b)