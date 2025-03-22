#occurence of value in string

str=input("Enter a string: ")
lst=[]
for i in str:
    num=str.count(i)
    if i not in lst:
        lst.append(i)
    else:
        continue
    print(f"{i} occurs {num} times")