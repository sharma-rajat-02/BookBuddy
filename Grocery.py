itemlst=[]
while True:
    try:
        items=input("")
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    else:
        itemlst.append(items.upper())
print(itemlst)
itemlst.sort()
while itemlst!=[]:
    for i in itemlst:
        x=itemlst.count(i)
        print(f"{x} {i}")
        for j in range(x):
            itemlst.remove(i)