/*
* BEE 1197 - Back to High School Physics - Level 1 - Mathematics
*/

import java.util.Scanner;

public class Bee1197 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int v, t;

        while (in.hasNextInt()) {
            v = in.nextInt();
            t = in.nextInt();
            System.out.println(2 * v * t);
        }
        in.close();
    }
}