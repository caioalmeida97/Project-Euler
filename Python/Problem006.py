import math;

sumSquare = 0;
squareSum = 0;
for i in range (101):
    sumSquare += math.pow(i, 2);
    squareSum += i;
squareSum = math.pow(squareSum, 2);
print(squareSum - sumSquare);
