#Choosing Number for Number Plate


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    alpha=list('QWERTYUIOPASDFGHJKLZXCVBNM')
    num=list('1234567890')
    platelist=list(s)
    l=len(s)
    if 2<=l<=6:
        if platelist[0] in alpha and platelist[1] in alpha:
            for i in platelist[2:6]:
                if i in alpha:
                    if platelist[platelist.index(i)-1] in num:
                        return False
                    else:
                        return True
                elif i in num:
                    if i=="0":
                        index=platelist.index("0")
                        if platelist[index-1] in alpha:
                            return False
                        elif platelist[index]==platelist[-1]:
                            return True
                        elif platelist[index-1] in num:
                            if platelist[-1] in alpha or platelist[index+1] in alpha:
                                return False
                            else:
                                return True
                    elif i in num:
                        index2=platelist.index(i)
                        if platelist[index2]==platelist[-1]:
                            return True
                        elif platelist[index2+1] in alpha:
                            return False
                else:
                    return False
    else:
        return False


main()