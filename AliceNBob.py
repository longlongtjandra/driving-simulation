def evenodd(x):
    return x%2

x=int(input("number of stones:"))

if evenodd(x)==1:
    print("alice")
else:
    print("Bob")
