import math;

for a in range (1, 500):
    for b in range(a + 1, 500):
        #print(a, b)
        if (math.sqrt(math.pow(a, 2) + math.pow(b, 2)) + a + b) == 1000:
            print(a * b * (1000 - a - b));
            break;
