import math;
from tqdm import tqdm

def getDivisors(n):
    div = [];
    for i in tqdm(range(1, n/2 + 1)): #tqdm outputs a progress bar for the loop
        if n % i == 0:
            div.append(i);
    return div;

divisors = [];
divisors = getDivisors(1000000);
print(len(divisors));
