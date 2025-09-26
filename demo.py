

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "this is a Prime ")
else:
    print(num, "this is not a Primeee")


num = int(input("Enter a numberrrrrrrrrrrr: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


