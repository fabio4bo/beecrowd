/*
* BEE 1221 - Fast Prime Number - Level 6 - Mathematics
*/

import java.util.Scanner;

public class Bee1221 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        long x;
        for (int i = 0; i < n; i++) {
            x = in.nextLong();
            if (optimusPrime(x))
                System.out.println("Prime");
            else
                System.out.println("Not Prime");
        }
        in.close();
    }

    public static boolean optimusPrime(long x) {
        if (x <= 1)
            return false;
        if (x == 2)
            return true;

        if (x > 2) {
            long raiz = (long) (Math.ceil(Math.sqrt(x)) + 1);
            for (long i = 2; i < raiz; i++) {
                if (x % i == 0)
                    return false;
            }
        }
        return true;
    }
}