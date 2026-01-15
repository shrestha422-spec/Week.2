n = int(input("Enter  n: "))
o = 0
p = 1
for i in range(n):
    o,p = p,o + p
    print("enter the number:", o)