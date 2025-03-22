#Print type of file and extension
name=input("Enter file name: ")
name=name.replace(" ","")
name=name.lower()
x=name.split(".")
y=x[-1]
match y:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif" | "png" :
        print("image/",y,sep='')
    case "pdf" | "zip":
        print("application/",y,sep='')
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
