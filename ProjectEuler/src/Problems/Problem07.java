package Problems;

class Problem07 {

    public static void main(String[] args) {
        /* What is the 10 001st prime number? */
        
        int i = 1;
        int prime_number = 1;
        while (true) {
            if (isPrime(prime_number)) {
                i++;
            }
            if (i == 10001) {
                System.out.println("The 10,001st prime number is: " + prime_number);
                return;
            }
            prime_number++;
        }
    }

    public static boolean isPrime(int num) {
        if ((num >= 2 && num % 2 == 0) || (num < 2)) {
            return false;
        }
        for (int i = 3; i < ((int) Math.sqrt(num) + 1); i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

}
