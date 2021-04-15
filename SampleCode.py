#while
x=1
while x<=9:
    #print(x)
    y = 1
    while y <= 9:
        #print(y)
        print(x, "*", y, "=", x * y)
        y = y + 1
    x = x + 1

# use for in -9*9
for x in range(1,10):
    print(x)
    for y in range(1,10):

        ans=x*y
        print(x,"*",y,"=",ans)