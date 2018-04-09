def collatzSequence(n):
    if n > 1000000:
        return [];
    else:
        ret = [n];
        while n > 1:
            if n % 2 == 0:
                ret.append(n / 2);
                n //= 2;
            else:
                ret.append(3 * n + 1);
                n = 3 * n + 1;
    return ret;

list = [];
number = 13;
longestChain = len(collatzSequence(number));
for i in range (13, 1000000):
    if(len(collatzSequence(i)) >= longestChain):
        number = i;
        print(number);
        longestChain = len(collatzSequence(number));

print(collatzSequence(number));
print("The number is: {0}, and the lenght is {1}".format(number, longestChain));


# #include <stdio.h>
#
# long next_collatz(long n) {
#     if (n % 2 == 0) {
#         return n / 2;
#     } else {
#         return 3 * n + 1;
#     }
# }
#
# long lencollatz(long start) {
#     if (start < 1) {
#         return 0;
#     } else if (start == 1) {
#         return 1;
#     }
#     long n = start;
#     long length = 1;
#     while (n != 1) {
#         n = next_collatz(n);
#         length++;
#     }
#     return length;
# }
#
# long main() {
#     long max_l = 0;
#     long max_i = 0;
#     long i;
#     for (i=1; i < 1000000; i++) {
#         long l = lencollatz(i);
#         if (l > max_l) {
#             max_l = l;
#             max_i = i;
#         }
#     }
#     printf("%ld\n", max_i);
#     return 0;
# }
