/*
* BEE 1805 - Natural Sum - Level 6 - Mathematics
*/

import java.util.Scanner;

public class Bee1805 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        long A1 = in.nextLong();
        long An = in.nextLong();
        in.close();
        long N = An - A1 + 1;
        long Sm = ((A1 + An) * N) / 2;

        System.out.println(Sm);
    }
}