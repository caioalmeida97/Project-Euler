from itertools import *

def comb(nums):
    for a in combinations(nums, 3): # Tentando fazer a combinatória dos números 1, 2 e 3
        print a

comb([1, 2, 3])
