#List Operations and Tuples

# a=['list','tup','str','tup']
# b=a.count('tup')
# print(b)
# print(len(a))
# c=[5,34,54,75,23,2,7,8,1,0,9,53,67]
# print(c.sort())
# d=("d",)
# print(f"{d} is a unit tuple")
# print(type(d))

#list of customer names who used to buy products through amazon. some of the customers will also buy through flipkart. 
# Determine the total no. of customers who buy through 
# 1. how many buy through online . 2. how many buy through flipkart. 3. How many buy through amazon. 4. display identical users


amazon=['ram','shyam','marry','geeta','joseph','gauri']
flipkart=['ram','gauri','shyam','sunny']
print(f'Number of customers that buy through amazon:{len(amazon)}')
print(f'Number of customers that buy through flipkart:{len(flipkart)}')
kart=[]
for i in amazon:
    if i in flipkart:
        kart.append(i)
        flipkart.remove(i)
print("Identical users:",kart)
print(f'Total Number of customers online:{len(flipkart)+len(amazon)}')
