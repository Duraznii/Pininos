age = 18
height = 1.75

#if
if age >= 18 and height >= 1.60:
    print("You can drink beer")

#or
if age >= 18 or height >= 1.60:
    print("You can drink beer")

#elif (else if)
if height < 1.60:
    print("You can't drink beer")
elif height < 1.70:
    print("You can drink beer") 
elif height < 1.80:
    print("You can drink beer and tequila") 
else:
    print("You can drink beer, tequila and vodka")

#exercise

credit_score = 700
last_purchase = "not paid"
current_credit = 900
if credit_score >= 700 and last_purchase == "paid" or current_credit >= 1000:
    print("You can buy a car")
