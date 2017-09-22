def distance (a,t):
    return (((a/2)*(t**2)))

def speed (a,t):
    return (a*t)


s=int(input("distance:"))
a=int(input("accelaration:"))
t=int(input("time:"))

for i in range(0,t+1):
    z=distance (a,i)
    v= speed (a,i)
    p=distance(a,i)
    result=z//10
    r=("*" * (int(result)))
    print("duration:"+(str(i)),"distance:",(str(r)))



    #if (v >= 60):
        #print("the person went over the speed limit.(max speed was"+str(v)+"m/s)")
        #break

    if((v >= 60) and (p>s)):
        print("the person reach the destination.(reached"+str(p)+"m)")
        print("the person went over the speed limit.(max speed was"+str(v)+"m/s)")
        break

    elif (v >= 60):
        print("the person went over the speed limit.(max speed was"+str(v)+"m/s)")
        break


    elif((p < s) and (i== t) ):
       print( "did not reach the destination.(reached"+str(p)+"m)")

    elif((p>s) and (i == t)):
        print( "the person reach the destination.(reached"+str(p)+"m)")

    elif((z >= s) and(v <= 60) ):
        print("the person reach the destination.(reached"+str(p)+"m)")
        print("the person did not go over the speed limit.(max speed was"+str(v)+"m/s)")
        break









