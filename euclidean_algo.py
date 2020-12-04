x = int(input("A: "))
y = int(input("B: "))

r=1

while(y!=0):
    m=x
    n=y    
    r=x%y 
    x=y
    y=r
    # print(f"{m}{m//n}*{n} + {r}")
    print(str(m) + "=" + str(m//n) + "*" + str(n) + "+" + str(r))
