#Electricity bill
# #1-100=0
# 100-200=2.55
# 200-300=3.55
# 300-400=4.55
# 400-infinity=6.55

unit=float(input("Enter units used: "))
if unit<=100:
    bill=0
    print(f"Your bill is {bill}")
elif 100<unit<=200:
    bill=0
    unit=unit-100
    bill+=unit*2.55
    print(f"Your bill is {bill}")
elif 200<unit<=300:
    bill=255
    unit=unit-200
    bill+=unit*3.55
    print(f"Your bill is {bill}")
elif 300<unit<=400:
    bill=255+355
    unit=unit-300
    bill+=unit*4.55
    print(f"Your bill is {bill}")
elif unit>400:
    bill=255+355+455
    unit=unit-100
    bill+=unit*6.55
    print(f"Your bill is {bill}")
else:
    print("Invalid input")