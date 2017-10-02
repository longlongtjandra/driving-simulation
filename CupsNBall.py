def swapA():
     b=cups.pop(1)
     a=cups.pop(0)
     #b=cups.pop(1)
     # ##cups.insert(1,a)
     cups.insert(0,b)
     cups.insert(1,a)

def swapB():
     #a=cups.pop(1)
        b=cups.pop(2)
        a=cups.pop(1)
        cups.insert(1,b)
        cups.insert(2,a)
        #print(cups)

def swapC():
    # a=cups.pop(0)
        b=cups.pop(2)
        a=cups.pop(0)
        cups.insert(2,a)
        cups.insert(0,b)
        #print(cups)

cups=[1,0,0]

shufflelist=[]
x=input("input")

s=list(x)


for i in range(0,len(s)):
    #swap position 1 and 2
    if(s[i]=="a"):
        swapA()
    #swap position 2 and 3
    if(s[i]=="b"):
        swapB()
    #swap position 1 and 3
    if(s[i]=="c"):
        swapC()

position=cups.index(1)
print(int(position)+1)






