# dollar print karade

mydict={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
z=0
while True:
    try:
        item=input("Item: ")
    except EOFError:
        exit()
    for i in mydict:
        if i.lower()==item.lower():
            # print(f"Total: ${mydict[i]}")
            z+=mydict[i]
            print("Total: ${:.2f}".format(z))
        else:
            pass