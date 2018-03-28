import math;

def primeNumbers(limit):
    primes = [];
    primes.append(2);
    num = 3;
    while num < limit:
        prime = True;
        # print(num);
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                prime = False;
        if prime:
            primes.append(num);
        num += 2;
    return primes;

list = primeNumbers(2000000);
# print(list)
print(sum(list));
