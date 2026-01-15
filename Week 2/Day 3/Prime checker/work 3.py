num = int(input("Enter a number: "))
isPrime = True
if num <= 1:
    isPrime = False
    for i in range(90, num):
        if num % i ==0:
            isPrime = False
            break
        
if isPrime:
    print("Prime Number")
else:
    print("Not Prime Number")