#TUPLES
#These are immutable
#these are may or may not be represented in curly brackets()

#acessing random elements from the TUPLES
city=('vizag','hyd','banglore')
print(city[1])
print(city[-1])

#concatenation=this will add the two tuples into one tuple
num=1,2,3,4,5,6,7,8,9,0
print(city+num)

#NESTING=this will nest two or more tuples in one tuples
nest=(city,num)
print(nest)

#REPETITION= it will repeat tuples as many times as mentioned.
print(nest*5)

#SLICING=IT WILL PRINT THE ELEMENTS OF SPECIFIC INDEXES mentioned
print(num[1:5])
print(num[1:])
print(num[::-1])

#UNPACKING=it will represent the individual elements in the form of tuple.
tuple('visakhapatnam')

#DELETING A tuple
def1=('a','b','c','d')

#converting list to tuple.
#ALTHOUGH we can't convert tuple to list
ABC=[1,2,3,4,5]
print(type(ABC))
DEF=tuple(ABC)
print(DEF)


