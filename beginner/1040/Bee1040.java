/*
* BEE 1040 - Average 3 - Level 5 - Beginner
*/

import java.text.DecimalFormat;
import java.util.Scanner;

public class Bee1040 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.0");

        double n1 = in.nextDouble();
        double n2 = in.nextDouble();
        double n3 = in.nextDouble();
        double n4 = in.nextDouble();

        double rAverage = (2 * n1 + 3 * n2 + 4 * n3 + n4) / 10;

        System.out.println("Media: " + df.format(rAverage));

        if (rAverage >= 7)
            System.out.println("Aluno aprovado.");
        else if (rAverage < 5)
            System.out.println("Aluno reprovado.");
        else {
            System.out.println("Aluno em exame.");
            double exameScore = in.nextDouble();
            System.out.println("Nota do exame: " + exameScore);
            double rEx = (exameScore + rAverage) / 2.0;

            if (rEx >= 5)
                System.out.println("Aluno aprovado.");
            else
                System.out.println("Aluno reprovado.");
            System.out.println("Media final: " + df.format(rEx));

        }
        in.close();
    }
}