fibonacci = [1, 2];
while (fibonacci[-1] < 4000000):
    fibonacci.append(fibonacci[-1] + fibonacci[-2]);

print(sum(number for number in fibonacci if (number % 2 == 0)));
