#print the letter in uppercase and prevent it from making new line
def uppercase(x):
    print(x.upper(),end="")

x=input("author:")
firletter=x[0]
uppercase(firletter)

# print the next character after the symbol "-"
for i in range(0,len(x)):
    if (x[i]== "-"):
        uppercase(x[i+1])
