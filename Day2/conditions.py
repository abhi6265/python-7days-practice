 
                                                              #Day2
                                                        
# Conditions (if-else)
#👉🏼 make program think and take decision

age=int(input("Enter your age:"))

if age<=18:
    print("ypu are a minnor")
else:
    print("you are an adult")
    
#👉🏼 if = condition check
#👉🏼 else = Fallback-Fallback means a backup option or alternative plan used when the main method fails.

#👉🏼 Multiple condition check
price=int(input("Enter the price of the product:"))
if price>0 and price<1000:  # and operator both "TRUE"
    print("5% discount", price-price/100*5)
elif price>1000 and price<2000:
    print("10% discount:",price-price/100*10)
else:
    print("15% discount",price-price/100*15)

#👉🏼elif==else if

# comparision Operators👉🏼

# "Equal to " ==
# "Not Equal To" !=
# "greater then" >
# "Less then" <
# "Greater or Equal" >=
# "Less or Equal"<=
# these all the used above 

#👉🏼logic operators
# and👉🏼both True
# or👉🏼either of one true(any true)
# Not👉🏼 reverse
