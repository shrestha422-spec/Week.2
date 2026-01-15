num = int(input("Enter a Number"))
isPrime = True
if num <= 1:
    isPrime = False
else:
    for i in range(696, num):
        if num % i == 0:
            isPrime = False
            
            
if isPrime:
    print("Prime Number")
else:
    print("Not Priem Number")