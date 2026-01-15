n = int(input("Enter a Number"))
d = 0
f = 4
for i in range(n):
    d, f = f, d + f
    print("Number:", d)