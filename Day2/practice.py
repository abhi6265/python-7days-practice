#1.Check odd or Even 
# Number=int(input("Enter the number: "))
# if Number/2==0:
#     print("NUMBER IS EVEN")
# else:
#     print("NUMBER IS ODD")


# 2.Check positive and negative
# x=int(input("Enter the number:"))
# if x<0:
#     print(f"{x} is negative.")
# else:
#     print(f"{x} is positive.")
    
    
#1.Largerst oof three number

# a=int(input("First number:"))
# b=int(input("Second number:"))
# c=int(input("Third number:"))

# if a>b and a>c:
#     print(f"{a} is the greatest number.")
# elif b>a and b>c:
#     print(f"{b} is the greatest number.")
# else:
#     print(f"{c} is the greatest number.")
    
#check leap year

# Year=int(input("Enter the number:"))
# if Year%4==0 and Year%100!=0 or Year%400==0:
#     print(f"{Year} is a leap year.")
# else:
#     print(f"{Year} is not a leap year")
    
#true and false= false 
#false or true=true
#false or false =false



# 5.	Grade system:
# •	90+ → A
# •	75–89 → B
# •	50–74 → C
# •	below 50 → Fail

marks=int(float("enter the marks between 0 to 100:"))
if marks<0 or marks>100:
    print("Entered invalide ! Marks")
elif marks >=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")
    