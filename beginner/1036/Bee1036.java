/*
* BEE 1036 - Bhaskara's Formula - Level 3 - Beginner
*/

// Submission: 28/10/17, 10:24 PM

import java.util.Scanner;

public class Bee1036 {

    public static void main(String[] args) {
        // https://www.todamateria.com.br/formula-de-bhaskara/

        Scanner entrada = new Scanner(System.in);

        double A = entrada.nextDouble();
        double B = entrada.nextDouble();
        double C = entrada.nextDouble();
        entrada.close();

        double delta = Math.pow(B, 2) - (4 * A * C);

        if (A > 0 && B > 0 && C > 0 && delta >= 0) {
            double R1 = (-B + (Math.sqrt(delta))) / (2 * A);
            double R2 = (-B - (Math.sqrt(delta))) / (2 * A);
            System.out.printf("R1 = %.5f\n", R1);
            System.out.printf("R2 = %.5f\n", R2);
        } else {
            System.out.print("Impossivel calcular\n");
        }
    }

}
