#Camel case = firstName, Snake_case = first_name
camelcase = input("camelCase: ")
camelcase=camelcase.lower()
camelcase=camelcase.replace(" ","")
a="preferred"
b="first"
c="name"
if b in camelcase:
    if a in camelcase:
        print("snake_case: ",a,"_",b,"_",c,sep="",end="")
    else:
        print("snake_case: ",b,"_",c,sep="",end="")
elif c in camelcase:
    print("sanke_case: ",c)
else:
    print("Inavlid Input")