import math;

def primeFactors(n):
    result = [];

    while(n % 2 == 0):
        result.append(2);
        n //= 2;

    limit = math.sqrt(n+1);
    i = 3;
    while i <= limit:
        if n % i == 0:
            result.append(i);
            n //= i;
            limit = math.sqrt(n+i);
        else:
            i += 2;
    if n != 1:
        result.append(n);
    return result;

print("The biggest prime factor is:");
print(max(primeFactors(600851475143)));
