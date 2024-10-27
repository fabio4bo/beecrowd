/*
* BEE 1012 - Area - Level 2 - Beginner
*/

// Submission: 27/10/17, 6:45 PM

import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("0.000");
        final double pi = 3.14159;
        Scanner entrada = new Scanner(System.in);
        double A, B, C;

        A = entrada.nextDouble();
        B = entrada.nextDouble();
        C = entrada.nextDouble();

        // Area do triangulo retangulo (a*c)/2
        double areaTR = (A * C) / 2;
        System.out.print("TRIANGULO: " + df.format(areaTR) + "\n");

        double areaC = pi * (C * C);
        System.out.print("CIRCULO: " + df.format(areaC) + "\n");

        double areaTz = ((A + B) * C) / 2;
        System.out.print("TRAPEZIO: " + df.format(areaTz) + "\n");

        double areaQ = B * B;
        System.out.print("QUADRADO: " + df.format(areaQ) + "\n");

        double areaR = A * B;
        System.out.print("RETANGULO: " + df.format(areaR) + "\n");

    }

}
