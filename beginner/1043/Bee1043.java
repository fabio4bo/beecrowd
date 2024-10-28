/*
* BEE 1043 - Triangle - Level 2 - Beginner
*/

import java.text.DecimalFormat;
import java.util.Scanner;

public class Bee1043 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");
        Double A = in.nextDouble();
        Double B = in.nextDouble();
        Double C = in.nextDouble();
        in.close();

        if (A + B > C && A + C > B && B + C > A) {
            double perimeter = A + B + C;
            System.out.println("Perimetro = " + df.format(perimeter));
        } else {
            double area = ((A + B) / 2) * C;
            System.out.println("Area = " + df.format(area));
        }
    }
}