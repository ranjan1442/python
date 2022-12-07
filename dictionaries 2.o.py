#clear() it will clear all the contents of the dictionary
player={'name':'virat','country':'india','age':32}
player.clear()
print(player)

#copy()
car={'brand':'audi',
     'model':'alto',
     'year':'2022'}
vechile=car.copy()
print(vechile)

#from keys()
dict={}
keys=('a','b','c')
values=(100,200,300)
w=dict.fromkeys(keys,values)
print(w)
for x in range(len(keys)):
    dict.update({keys[x]:values[x]})
print(dict)

#for iterate variables in dict.items():
veg={'rice':100,'mushrooms':200,'burger':50}
for a,b in veg.items():
    print(a,b)
    
#for iterate variables in dict.values():
for x in veg.values():
      print(x)
for x in veg.keys():
    print(x)
Keys=[]
Values=[]
Dict={}
n=int(input('enter the no of ordered items='))
for x in range(n):
    name=input('enterdish name=')
    price=int(input('enter the dish price'))
    keys.append(name)
    values.append(price)
print('coustmer orderr following dishes')
print(keys)

for x in range(n):
    dict.update({keys[x]:values[x]})
total=0
for p in dict.values():
    total=total+p
for x,y in dict.items():
    print(x,':',y)
print('total':,total)
   
