#Dictionaries
import time
dict={'Name':'Rajat Sharma',
      'Reg No.':'23BAI10159',
      'School': 'SCAI',
      'Branch':'CSE-AIML',
      'University':'VIT Bhopal University'}
starttime=time.time()
copy=dict.copy()
dict.clear()
copy.pop('School')
print(dict)
print(copy)
for i in copy:
    print(copy[i])
print(f'Length of the dictionary is {len(copy)}')
print()
print(copy.get('Name'),copy.get('Reg No.'),sep=' : ')
x=copy.fromkeys('ABCD','1234')
x['A']='0123'
x.pop('A')
print(x)
print(x.items())
print(x.keys())
endtime=time.time()
total_time=time.ctime(endtime)
print(starttime)
print(endtime)
print(total_time)
x.setdefault('X','1234')
x.update({'A':'1234'})
print(x)
print(x.values())
y=list(x)
print(y)