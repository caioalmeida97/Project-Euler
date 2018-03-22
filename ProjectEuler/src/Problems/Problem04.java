package Problems;

public class Problem04 {

    public static void main(String[] args) {
        /*
        A palindromic number reads the same both ways.
        The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
        Find the largest palindrome made from the product of two 3-digit numbers.
         */

        int previous, next;
        double result = 0;
        int k = 0, l = 0;
        for (int i = 100; i < 999; i++) {
            for (int j = i; j < 1000; j++) {
                if (isPalindrome(i * j)) {
                    if (i * j > result) {
                        result = i * j;
                        k = i;
                        l = j;
                    }
                }
            }
        }

        System.out.println("The biggest palindrome is: [" + result + "], and the 3-digit numbers are: [" + k + ", " + l + "]");

    }

    public static boolean isPalindrome(int number) {
        String num = Integer.toString(number);
        String inverse = "";
        int index = num.length() - 1;
        for (int i = 0; i < num.length(); i++) {
            inverse += num.charAt(index);
            index--;
        }

        if (num.compareTo(inverse) == 0) {
            return true;
        }

        return false;
    }

}
