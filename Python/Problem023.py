from itertools import *

def divisors(n):
    div = [];
    for i in range(1, n/2 + 1):
        if(n % i == 0):
            div.append(i);
    return div;

def classify(n):
    divSum = sum(divisors(n));
    if divSum < n:
        return -1; # Deficient number
    elif divSum == n:
        return 0;  # Perfect number
    elif divSum > n:
        return -1; # Abundant number

limit = 28123; # All numbers above 28123 can be written by the sum of 2 abundant numbers
abundantNums = [];
# for i in range(1, limit):
#     if abundant(i):
#         abundant_nums.append(i);

# print(abundant_nums);
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10]
z = [a for a in x if a not in y]
for a in combinations(x, 2):
    print a
# print z
