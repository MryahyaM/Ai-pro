stock = [{"name":"tomato","price":4, "stock":100},
{"name":"carrot","price":8, "stock":80},
{"name":"onion","price":11, "stock":70},
{"name":"potato","price":19, "stock":50}]
def preview():
    print("\n\n==========================================")
    print('Name\t\tPrice\t\tStock\n')
    print("==========================================")

    for item in stock:
        print("{0}\t\t {1}/=\t\t {2}\n".format(item['name'], item['price'], item['stock']))
    print("==========================================")
def create():
    print("\n[*] ADDING A NEW STOCK\n\n")
    print("        before we begin 'Stock' stands for how many items you will keep")
    print("        and 'category' is the type of vegetables/items to keep \n")
    print("[+] Let's begin:\n\n")
    stoc = int(input(">>> How many vegetables will you keep?\n  (CAEGORY): "))
    for i in range(stoc):
        name = input(">>>>ITEM: ")
        price = int(input(">>>>PRICE: "))
        st = int(input(">>>>STOCK: "))
        dictn = {'name':name, 'price':price, 'stock':st}
        stock.append(dictn)
        print("[+] Record added to database")
    preview()

def amount(item,quantity):
    for element in stock:
        if item == element['name']:
            total = int(quantity) * int(element['price'])
            break
    print("\n=========================================")
    print(f"the total amount for {item} is {total}"+"/=")
    print("==========================================")
    main()

def buy(item,quantity):
    for it in stock:
        if item == it['name']:
            newStock = it['stock'] - int(quantity)
            it['stock'] = newStock
            break
    amount(item,quantity)

def menu():
    preview()
    item = ""
    quantity = 0
    item = input("What is user buying : ")
    if item == "stop":
        main()
    else:
        quantity = int(input("Quantity: "))
        fetch_item(item,quantity)

def fetch_item(item,quantity):
    for l in stock:
        if item == l['name']:
            if int(quantity) == int(l['stock']) or int(quantity) < int(l['stock']):
                buy(item,quantity)
            else:
                diff = l['stock']
                print(f"[!] Can't purchase this items. Only {diff} items are available now in the stock"+"\n")
                break
    if item != l['name']:
        print(f"{item} is not in the list")

def update():
    item = ""
    quantity = 0
    print('''

        [+] 1) INCREASE STOCK
        [+] 2) REDUCE STOCK

    ''')
    choice = int(input("Choice: "))
    if choice == 1:
        item = input("Enter the item to Increase: ")
        quantity = int(input("Quantity: "))
        for element in stock:
            if item == element['name']:
                newstock = element['stock']+ quantity
                element['stock'] = newstock
                print(f"\n [+]{item} IS INCREASED BY {quantity}")
                break
        preview()
    if choice == 2:
        item = input("Enter the item to Reduce: ")
        quantity = int(input("Quantity: "))
        for element in stock:
            if item == element['name']:
                newstock = element['stock'] - quantity
                element['stock'] = newstock
                print(f"\n [+]{item} IS REDUCED BY {quantity}")
                break
        preview()

def main():
	while True:
		print('''


            [+] 1) ADD STOCK
            [+] 2) START PURCHASE 
            [+] 3) UPDATE STOCK
            [+] 4) EXIT


		''', end="")
		choice = int(input("Choice:"))
		if choice == 1:
			create()
		elif choice == 2:
			menu()
		elif choice == 3:
		    update()
		else:
		    exit()

main()
