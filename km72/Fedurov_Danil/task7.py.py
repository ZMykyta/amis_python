
x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))
if (x1+x2)%2==0 and (y1+y2)%2==0:
    print("YES")
elif (x1+x2)%2!=0 and (y1+y2)%2!=0:
    print("YES")
else:
    print("NO")