# # Create list of 5 numbers and print them
num=[12,34,53,1,3,4]
print(num)
#length
print(len(num))
#min
print(min(num))
#max
print(max(num))

# Reverse
#in_place reverse(modifies original list) 
num.reverse()
print(num)

# Reverse
# crease a reverse copey of original list(original will stay same)
rev=num[::-1]
print(rev)
print(num)


# Count how many times a number appears

list1=[1,32,42,1,23,32,43,3,4,34,32,2]
num=int(input("enter the number which ocrance count you want:"))
count=0
for i in (list1):
    if num==i:
        count+=1
print(f"{num} apears {count} times")

#count function

list1=[1,32,42,1,23,32,43,3,4,34,32,2]
num=int(input("enter the number which ocrance count you want:"))

print(f"{num} apeers {list1.count(num)} times")



# removing duplicate  from list

list1 = [1, 2, 2, 3, 4, 2, 5]

i = 0
while i < len(list1):
    j = i + 1
    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)
        else:
            j += 1
    i += 1

print(list1)



list1 = [1, 2, 2, 3, 4, 2, 5]

print(list(set(list1))) #not in order



    