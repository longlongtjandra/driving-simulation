#function to calculate the modulus of 42
def modulus42(x):
    return x%42

numlist=[]
resultlist=[]
setlist=[]
#to collect 10 input
for i in range (0,10):
    x=int(input("input"))
    numlist.append(x)
#to use modulus of 42 on input
for a in range(0,10):
    number=numlist.pop()
    result=modulus42(number)
    resultlist.append(result)

# to see the amount of distinct result
for y in set(resultlist):
    setlist.append(y)
#print the distinct values
print("distinct values:"+str(len(setlist)))






