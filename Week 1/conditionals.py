temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


#ternary operator
age = 22
message = "Eligbile" if age >= 18 else "Not Eligible"
print(message)

#conditionals and,or,not. Determine eligibility of loan
high_income = False
good_credit = True
student = True

if(high_income or good_credit) and not student:
    print("EEEEEligible")
else:
    print("Not eligible")

#short circuit
if(high_income and good_credit) and not student:
    print("Short circuit eigible")
else:
    print("Short circuit Not eligible")

#chaining comparison operators
new_age = 22
if 18 <= new_age < 65:
    print("new age is Eligible")