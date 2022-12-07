#LIST SLICING
#LIST[START INDEX:STOP INDEX:STEP SIZE]

l=[12,34,56,75,68,223,445,]
l1=l[2:4:1]
print(l1)
l2=l[-1:-11:-2]
print(l2)

#SLICING SHORTCUTS
print(l[2:])
print(l[ :5])
print(l[ : :3])
print(l[ :-6])
print(l[ : :-1])
print(l[-1:-7])
print(l[-10:6])
print(l[-10:-6])