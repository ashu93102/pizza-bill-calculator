#pizza bill calculator

print("Thankyou for choosing python pizza delivery")

size = input("What size pizza do you want? S, M, or L,\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").upper()

bill = 0

# #samll pizza price = 15
# #Medium pizza price = 20
# #Large pizza price = 25
# # pepperoni for small = 2
# # pepperoni for medium and large = 3
# #extra cheese = 1


#for small pizza bill
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1

#for medium pizza bill
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

#for large pizza bill
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1


print(f"Your final bill is: ${bill}.")


