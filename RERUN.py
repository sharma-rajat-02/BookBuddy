def renum(funct):
    x='Yes'
    while True:
        if x=='Yes':
            y=input("Do you want to use the program again? {Yes,No} : ")
            y=y.capitalize()
            x=x.replace("Yes",y)
            funct
        elif x=='No':
            print("Thankyou for using the program!")
            break