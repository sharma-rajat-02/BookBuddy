monthslst=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        day=input("Date: ")
    except ValueError:
        pass
    else:
        if "/" in day:
                day=day.replace(" ","")
                day=day.split("/")
                if day[0] is not str:
                    if int(day[1])<=31:
                        try:
                            if int(day[0])<=12:
                                if len(day[2])==4:
                                    print(f"{day[2]}-{int(day[0]):02}-{int(day[1]):02}")
                                    break
                                else:
                                    pass
                            else:
                                pass
                        except ValueError:
                            pass
                    else:
                        pass
                else:
                    pass
        elif "," in day:
            day=day.replace(",","")
            day=day.split(" ")
            if day[0].capitalize() in monthslst:
                day[0]=(monthslst.index(day[0].capitalize()))+1
                if int(day[1])<=31:
                    if len(day[2])==4:
                        print(f"{day[2]}-{int(day[0]):02}-{int(day[1]):02}")
                        break
                    else:
                        pass
                else:
                    pass
            else:
                pass