/*
* BEE 1921 - Guilherme and His Kites - Level 3 - Mathematics
*/

import java.util.Scanner;

public class Bee1921 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        long N = in.nextInt();
        in.close();

        System.out.println(N * (N - 3) / 2);
    }
}