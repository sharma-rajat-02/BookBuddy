#Using match perfectly instead of if else

deep=input("What is the answer to the Great Question of Life, the Universe and Everything? ")
deep=deep.replace("-","")
deep=deep.replace(" ","")
deep=deep.lower()
match deep:
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
