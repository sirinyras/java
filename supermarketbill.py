from datetime import datetime

name = input("Enter your name: ")

lists = '''
RICE    RS 20/KG
SUGAR   RS 30/KG
SALT    RS 15/KG
OIL     RS 200/LITER
PANEER  RS 80/KG
CLOVES  RS 500/KG
BRUSH   RS 45/EACH
'''

# prices
items = {
    'RICE': 20,
    'SUGAR': 30,
    'SALT': 15,
    'OIL': 200,
    'PANEER': 80,
    'CLOVES': 500,
    'BRUSH': 45
}

price_list = []
ilist = []
qlist = []
plist = []

total_price = 0
gst = 0
final_price = 0

option = int(input("Press 1 to see items list: "))
if option == 1:
    print(lists)

for i in range(len(items)):
    inp = int(input("Press 1 to buy or 2 to exit: "))
    if inp == 2:
        break

    item = input("Enter item name: ").upper()
    quantity = int(input("Enter quantity: "))

    if item in items:
        price = quantity * items[item]
        total_price += price

        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)

    else:
        print("Sorry, item not available")

# bill calculation
gst = (total_price * 5) / 100
final_price = total_price + gst

print("=" * 75)
print(" SIRI MART".center(75))
print("ooty".center(75))
print("=" * 75)

print(f"Name : {name}".ljust(40) + f"Date : {datetime.now()}")
print("-" * 75)

print(f"{'S.No':<6}{'Item':<20}{'Qty':<10}{'Price':<10}")
print("-" * 75)

for i in range(len(ilist)):
    print(f"{i+1:<6}{ilist[i]:<20}{qlist[i]:<10}{plist[i]:<10}")

print("-" * 75)
print(f"{'Total Amount':>55} : Rs {total_price}")
print(f"{'GST (5%)':>55} : Rs {gst}")
print("-" * 75)
print(f"{'Final Amount':>55} : Rs {final_price}")
print("=" * 75)

print("Thanks for visiting".center(75))
print("=" * 75)