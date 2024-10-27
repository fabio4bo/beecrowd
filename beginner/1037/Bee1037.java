/*
* BEE 1037 - Interval - Level 3 - Beginner
*/

// Submission: 27/10/17, 8:31 PM

import java.util.Scanner;

public class Bee1037 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double A;

        A = entrada.nextDouble();

        if(A >= 0 && A <= 25)
            System.out.print("Intervalo [0,25]\n");
        else if(A > 25 && A <=50)
                System.out.print("Intervalo (25,50]\n");
                else if(A > 50 && A <=75)
                    System.out.print("Intervalo (50,75]\n");
                else if(A > 75 && A<=100)
                        System.out.print("Intervalo (75,100]\n");
                    else
                        System.out.print("Fora de intervalo\n");

    }

}
