package Problems;

import java.util.ArrayList;

public class Problem03 {

    public static void main(String[] args) {
        /* What is the largest prime factor of the number 600851475143 ? */

        long n = 600851475143L;
        int biggest_divisor;
        ArrayList divisors = new ArrayList();
        divisors = prime_factors(n);
        System.out.println("The divisors for " + n + " are:");
        for (Object d : divisors) {
            System.out.println("\t->" + d);
        }
    }

    public static ArrayList prime_factors(long n) {
        ArrayList prime_factors = new ArrayList();
        while (n % 2 == 0) {
            prime_factors.add(2);
        }
        int limit = (int) Math.sqrt(n+1), i = 3;
        while (i <= limit){
            if (n % i == 0){
                prime_factors.add(i);
                n /= i;
                limit = (int) Math.sqrt(n+i);
            } else
                i += 2;
        }
        if(n!= 1)
            prime_factors.add(n);
        
        return prime_factors;
    }
    
}
