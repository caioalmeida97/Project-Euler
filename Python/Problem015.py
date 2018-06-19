from gmpy2 import comb

# Look at Problem015.mkd to understand why the possibilities are given by
# the combination of (40, 20)
possibilities = comb(2*20, 20);
print(possibilities);
