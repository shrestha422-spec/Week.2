n = int(input("Enter a Number: "))

q = 0
e = 1

for i in range(n):
    q, e = e, q + e
    print("Fibonacci Number:", q)