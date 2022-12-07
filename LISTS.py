 
fruit=["apple","guava","apple"]
print(fruit[0])
number=[1,2,3]
nos=fruit+number
print(nos)
mos=nos*3
print(mos)
print(mos[4])

#operations on list
#len()=count the number of elemrnts in list.
#min()=print the minimum value of the element in the list.
#max()=print the maximum value of the element in the list.
#sum()=print the sum of all integers  or float elements of the list.
#del()=delete the list along with the elements permanently.
l=[1,2,3,4,5,6,]
print(l)
print(l)
print(len(l))
print(min(l))
print(max(l))
print(sum(l))
del(l)

#List Methods
#append()=adding element at the of the list.
l=[12345678,34567,234578]
l.append(7)
print(l)

#Insert()=inserting the element at he specific index.
m=[2,3,4,56]
m.insert(3,77)
print(m)

#Remove()=removing the elements from the index.
v=[3,2,5,7,9,10,2,3]
v.remove(2)
print(v)
# *Note= here only first 2 will delete, second 2 will not delete.

#pop()=pop method will delete the elements,if we just specify the index position.
# *Note=if we does not specify the index position, by default it will it will delete the last. 
n=[2,3,4,5,6]
n.pop(2)
print(n)
n.pop()
print(n)

#Index()=it will give us element position.
x=[1,2,3,5,4,5,6]
print(x.index(5))

#Extend()= it will add the list at the end of the another list.
s=[1,2,3]
p=[4,5,6]
s.extend(p)
print(s)

#Sort()=it will arrange the elements in ascending order
p=[5,4,3,2,1]
p.sort()
print(p)

#Count()=it will tell us number of times a specific given element is repeating.
f=[1,2,2,2,3,4,5,2]
c=f.count(2)
print(c)

#Copy()=ex.it will change the second of the s as 9
s=[1,8,3,4,5]
s[2]=9
print(s)

#Reverse()= it will the elements in the list.
d=[1,2,3,4,57,8]
d.reverse()
print(d)


#processing of list using "for" loop
country=['india','france','china','usa']
for x in range(len(country)):
    print(country[x])
for x in country:
    print(x.upper())
for x in country:
    print(x.title())
    
country=[]
n=int(input('enter how many elements you want to add in the LIST='))
for x in range(n):
    c=input('enter new countryname=')
    country.append(c)
for a in country:
    print(a.upper())