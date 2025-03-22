#Tell what meal to eat
def main():
    x=input("What time is it? ")
    convert(x)
def convert(time):
    time=time.replace(" ","")
    time=time.split(":")
    a=float(time[0])
    b=time[1]
    if "a.m" in b:
        b=b.replace("a.m","")
        b=float(int(b)/60)
        c=a+b
    elif "p.m" in b:
        b=b.replace("p.m","")
        b=float(int(b)/60)
        c=a+b
        if 6<=c<=7:
            print("Dinner Time")
        elif 12<=c<=13:
            print("Lunch Time")
    else:
        b=float(int(b)/60)
        c=a+b
        if 7<=c<=8:
            print("Breakfast Time")
        elif 12<=c<=13:
            print("Lunch Time")
        elif 18<=c<=19:
            print("Dinner Time")
    return c
if __name__ == "__main__":
    main()
