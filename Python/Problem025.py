def fibonacci(size):
    fibonacciSeq = [];
    for i in range(size):
        if i == 0 or i == 1:
            fibonacciSeq.append(1);
        else:
            num = fibonacciSeq[i-2] + fibonacciSeq[i-1];
            fibonacciSeq.append(num)
    return fibonacciSeq;

k = 1;
sizeNum = 0;
while (sizeNum < 1000):
    sequence = fibonacci(k);
    # print(sequence);
    num = sequence[-1]
    sizeNum = len(str(num))
    k += 1;
k -= 1;
print [num, k]
