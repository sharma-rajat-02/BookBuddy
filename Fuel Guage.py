def main():
    x=get_int()
    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(int(x),"%",sep="")
def get_int():
    while True:
        try:
            fraction=input("Fraction: ")
            fraction=fraction.split("/")
            f=(int(fraction[0])/int(fraction[1]))*100
            if f>100:
                pass
            else:
                if f-int(f)>0.5:
                    return int(f+1)
                else:
                    return int(f)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
main()
            