n = int(input("Enter a Number: "))
a = 0
b = 4

for i in range(n):
    a, b = b, a + b
    print("Number", a)