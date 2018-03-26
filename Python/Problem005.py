def is_divisible_to(number, x):
    # print("Number: " + str(number));
    # print("X: " + str(x));
    for i in reversed(list(range(1, x+1))):
        if number % i != 0:
            return False;
    return True;

def divisible_to(x):
    if x < 1:
        return False;
    elif x == 1:
        return 1;
    else:
        step = divisible_to(x-1);
        # print("The step is: " + str(step));
        number = 0;
        found = False;
        while not found:
            number += step;
            found = is_divisible_to(number, x);
        return number;

# Works until 997
print(divisible_to(20));
