import math;

def getDivisors(n):
    div = [1];
    if n == 0:
        return [];
    elif n == 1:
        return [1];
    else:
        div.append(n);
        print(n)
        while n > 1:
            if n % 2 == 0:
                div.append(2);
                n //= 2;
            else:
                for i in reversed(list(range(3, n))):
                    if n % i == 0:
                        div.append(i);
                        n //= i;
                    else:
                        break;
    return div;

divisors = [];
divisors = getDivisors(10);
print(divisors)
