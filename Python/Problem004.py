import math;

def isPalindrome(n):
    return (str(n) == str(n)[::-1]);

palindromeProducts = [];
for i in range (100, 1000):
    for j in range (100, 1000):
        if(isPalindrome(i*j)):
            palindromeProducts.append(i*j);

print(max(palindromeProducts));
