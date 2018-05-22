def amicable(n):
    sum_div = sum_divisors(n);
    if sum_div == n:
        return False;
    return(sum_divisors(sum_div) == n);

def sum_divisors(n):
    return sum(divisors(n));

def divisors(n):
    div = [];
    for i in range(1, n/2 + 1):
        if(n % i == 0):
            div.append(i);
    return div;

amicable_numbers = []
for i in range(10000):
    if(amicable(i)):
        print i, divisors(i);
        amicable_numbers.append(i);

print sum(amicable_numbers)
