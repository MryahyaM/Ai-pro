stock = [{"name": "tomato", "buying": 4, "selling": 10, "stock": 100},
{"name": "carrot", "buying": 8, "selling": 12,  "stock": 80},
{"name": "onion", "buying": 11, "selling": 18, "stock": 70},
{"name": "potato", "buying": 19, "selling": 25,  "stock": 50}]
profits = []

def preview():
    print("\n\n================================================================")
    print('Name\t\tbuying\t\tselling\t\tStock\n')
    print("================================================================")

    for item in stock:
        print("{0}\t\t {1}/=\t\t {2}/=\t\t {3}\n".format(
            item['name'], item['buying'], item['selling'], item['stock']))
    print("================================================================")


def create():
    print("\n[*] ADDING A NEW STOCK")
    print("[+] Let's begin:\n")
    stoc = int(input(">>> How many vegetables will you keep?\n  (CAEGORY): "))
    for i in range(stoc):
        name = input(">>>>ITEM: ")
        buying = int(input(">>>>BUYING PRICE: "))
        selling = int(input(">>>>SELLING PRICE"))
        stocs = int(input(">>>>STOCK: "))
        dictn = {'name': name, 'buying': buying,'selling': selling, 'stock': stocs}
        stock.append(dictn)
        print("[+] Record added to database")
    preview()


def profit(item, quantity):
    pro = ""
    for element in stock:
        if item == element['name']:
            diff_profit = (int(element['selling']) - int(element['buying'])) * int(quantity)
            pro = diff_profit
            profits.append(pro)
            prof = sum(x for x in profits)
            print("\n=============================================================")
            print(f'\t\t The total profit is {prof} /=')
            print("=============================================================\n")
            break
    main()


def amount(item, quantity):
    for element in stock:
        if item == element['name']:
            total = int(quantity) * int(element['selling'])
            break
    print("\n=============================================================")
    print(f"\t\tthe total amount for {item} is  {total}"+"/=")
    print("=============================================================")
    profit(item, quantity)


def buy(item, quantity):
    for it in stock:
        if item == it['name']:
            newStock = it['stock'] - int(quantity)
            it['stock'] = newStock
            break
    amount(item, quantity)


def menu():
    preview()
    item = ""
    quantity = 0
    item = input("\nWhat is user buying : ")
    if item == "stop":
            main()
    else:
        quantity = int(input("Quantity: "))
        fetch_item(item, quantity)


def fetch_item(item, quantity):
    for l in stock:
        if item == l['name']:
            if int(quantity) == int(l['stock']) or int(quantity) < int(l['stock']):
                buy(item, quantity)
            else:
                diff = l['stock']
                print(
                    f"[!] Can't purchase this items. Only {diff} items are available now in the stock"+"\n")
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
                newstock = element['stock'] + quantity
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


            [+] 1) ADD NEW STOCK
            [+] 2) START PURCHASE 
            [+] 3) UPDATE STOCK
            [+] 4) VIEW STOCK
            [+] 5) EXIT


		''', end="")
        choice = int(input("Choice:"))
        if choice == 1:
            create()
        elif choice == 2:
            menu()
        elif choice == 3:
            update()
        elif choice == 4:
            preview()
        else:
            exit()


main()
