/*
* BEE 1198 - Hashmat the Brave Warrior - Level 5 - Mathematics
*/

import java.util.Scanner;

public class Bee1198 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long x, y;
        while (in.hasNextLong()) {
            x = in.nextLong();
            y = in.nextLong();
            System.out.println(Math.abs(x - y));
        }
        in.close();
    }
}