#Gretting ke liye puchna hoga 

greet=input("How were you greeted? ")
greet=greet.lower()
greet=greet.replace(" ","")
g=list(greet)
if "hello" in greet:
    print("$0")
elif g[0]=="h":
    print("$20")
else:
    print("$100")
