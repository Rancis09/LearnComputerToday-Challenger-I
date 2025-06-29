bill = int(input("How much is the total bill? "))
diners = int(input("How many diners are there? "))
split = bill / diners
print("Each diner should pay: ₱" + str(split))