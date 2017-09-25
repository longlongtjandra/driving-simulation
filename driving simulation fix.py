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




    if ( (v>60) and (z>=s) and (i == t)):
        print("the person went over the speed limit.(Max speed was"+ (str(v))+"m/s)")
        print("the person reached the destination. (reached"+str(z)+"m/s)")

    elif( (v <=60) and (z>=s) and (i==t)):
        print("the person did not go over the speed limit. (Max speed was"+ str(v)+"m)")
        print("the person reached the destination. (reached"+str(z)+"m/s)")

    elif( (v>60) and (z<s) and (i==t)):
        print("the person went over the speed limit.(Max speed was"+ str(v)+"m/s)")
        print("the person did not reached the destination. (reached"+str(z)+"m)")

    elif( (v<=60)and (z<s) and (i==t)):
        print("the person did not go over the speed limit. (Max speed was"+ str(v)+"m/s)")
        print("the person did not reached the destination. (Reached"+str(z)+"m)")


