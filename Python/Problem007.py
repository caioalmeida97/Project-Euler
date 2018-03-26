import math;

def isPrime(n):
    if n == 2:
        return True;
    if n % 2 == 0 and n != 2 or n == 1:
        return False;
    for i in range (3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;
    return True;

cont = 0;
number = 2;
while cont < 10001:
    if isPrime(number):
        cont += 1;
    number += 1;

number -= 1;
print(number);
