import math
def ctp(x,y):
    print ("Cartesian: ({a},{b})".format(a=x,b=y))
    print ("Polar: r ={a} Theta ={b} degrees".format(a=math.sqrt(pow(x,2) +pow(y,2)),b=math.degrees(math.atan(y/x))))
def ptc(r,t):
    print("polar:({a},{b})".format(a=r,b=t))
    print(f"Cartesian: x={r*math.cos(t)}, y={r*math.sin(t)}")    
choice=int(input("choice 1-2 (1-cartesian to polar,2-polar to cartesian):"))
if choice==1:
    x=float(input("x-coord:"))
    y=float(input("y-coord:"))
    try:
        ctp(x,y)
    except ZeroDivisionError:
        print("zero div error")
elif choice==2:
    r=float(input("r:"))
    t=float(input("theta(in radians):"))
    ptc(r,t)
