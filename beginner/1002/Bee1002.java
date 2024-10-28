/*
* BEE 1002 - Area of a Circle - Level 4 - Beginner
*/

import java.text.DecimalFormat;
import java.util.Scanner;

public class Bee1002 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0000");
        final double PI = 3.14159;
        double r = in.nextDouble();
        in.close();

        double c_area = PI * Math.pow(r, 2.0);

        System.out.println("A=" + df.format(c_area));
    }
}