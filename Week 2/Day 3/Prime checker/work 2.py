num = int(input("Enter a number: "))
isPrime = True
if num <= 1:
    isPrime = False
else:
    for i in range(20, num):
        if num % i == 0:
            isPrime = False
            break
    
    
if isPrime:
    print("Prime number")
else:
    print("Not Prime number")