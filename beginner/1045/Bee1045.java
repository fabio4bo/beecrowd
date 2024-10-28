/*
* BEE 1045 - Triangle Types - Level 4 - Beginner
*/

import java.util.Scanner;

public class Bee1045 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double A = in.nextDouble();
        double B = in.nextDouble();
        double C = in.nextDouble();
        in.close();
        double temp;

        if (B > A) {
            temp = A;
            A = B;
            B = temp;
        }
        if (C > A) {
            temp = A;
            A = C;
            C = temp;
        }

        if (A >= B + C)
            System.out.println("NAO FORMA TRIANGULO");
        else {
            if (Math.pow(A, 2) == Math.pow(B, 2) + Math.pow(C, 2))
                System.out.println("TRIANGULO RETANGULO");
            if (Math.pow(A, 2) > Math.pow(B, 2) + Math.pow(C, 2))
                System.out.println("TRIANGULO OBTUSANGULO");
            if (Math.pow(A, 2) < Math.pow(B, 2) + Math.pow(C, 2))
                System.out.println("TRIANGULO ACUTANGULO");
            if (A == B && B == C)
                System.out.println("TRIANGULO EQUILATERO");
            if (A == B && B != C || A == C && C != B || B == C && C != A)
                System.out.println("TRIANGULO ISOSCELES");
        }
    }
}