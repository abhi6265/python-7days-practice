# # print counting 1-100
# for i in range(1,101):
#     print(i)
    

# #print all even number between 1-100
# for i in range(1,101):
#     if i%2==0:
#         print(i)
        
        
# #print odd number between 1-50
# for i in range(1,51,2):
#     print(i)
    
    
#Sum of first n number
# n=int(input())
# total=0
# for i in range(n):
#     total+=i
# print(total)

#Factorial of any number
# n=int(input())
# factorial=1
# for i in range(n):
#     factorial*=n-i
# print(factorial)

#multiplication Table

# num=int(input())

# for i in range(1,11):
#     print(f"{num}×{i}={num*i}")


#prime number check

# num=int(input())
# i=2
# is_prime=True
# for i in range(num):
#     if num%2==0:
#         is_prime=False
#     i+=1
# if is_prime and i>1:
#     print("prime")
# else:
#     print("Not prime")
    
    
# n=int(input())
# i=2
# is_prime=True
# while i<n:
#     if n%2==0:
#         is_prime=False
#     i=i+1
# if is_prime and i>1:
#     print("prime")
# else:
#     print("Not Prime")


n = int(input())

if n > 0:
    num = n
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print(total)