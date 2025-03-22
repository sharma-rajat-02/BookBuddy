#Importing modules
import random
import RERUN

def rannum():
    num=random.randint(1,10)
    print(num)
if RERUN.renum(rannum())=="Yes":
    rannum()
