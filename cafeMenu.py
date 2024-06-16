menu = {
    'pizza' : 230,
    'pasta' : 110,
    'burger' : 99,
    'salad' : 45,
    'coffee' : 120,
}



#greet

print("Welcome TO PYTHON Restaurant")
print("pizza : RS 230\npasta : RS 110\nburger : RS 99\nsalad : RS 45\ncoffee : RS 120")

order_total = 0

item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not avaliable yet")

another_order = input("do you want to add another item(yes/no)")

if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item{item_2} is not avaliable ")

print(f"the total amount of items to pay is {order_total}")            