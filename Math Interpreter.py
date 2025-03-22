#Math interpreter
i=input("Expression: ")
if "+" in i:
        i=i.replace(" ","")
        a=i.split("+")
        e=int(a[0])+int(a[1])
        print(float(e))
elif "-" in i:
        i=i.replace(" ","")
        b=i.split("-")
        f=int(b[0])-int(b[1])
        print(float(f))
elif "*" in i:
        i=i.replace(" ","")
        c=i.split("*")
        g=int(c[0])*int(c[1])
        print(float(g))
elif "/" in i:
        i=i.replace(" ","")
        d=i.split("/")
        if d[1]=="0":
            print("Denominator cannot be 0")
            exit()
        else:
            h=int(d[0])/int(d[1])
            print(float(h))
else:
        print("Please enter valid operation")
