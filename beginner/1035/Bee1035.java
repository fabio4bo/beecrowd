/*
* BEE 1035 - Selection Test 1 - Level 2 - Beginner
*/
// Submission: 27/10/17, 6:02 PM

import java.util.Scanner;

public class Bee1035 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int A = entrada.nextInt();
        int B = entrada.nextInt();
        int C = entrada.nextInt();
        int D = entrada.nextInt();
        entrada.close();

        if (B > C && D > A && (C + D) > (A + B) && (C > 0 && D > 0) && A % 2 == 0)
            System.out.print("Valores aceitos\n");
        else
            System.out.print("Valores nao aceitos\n");

    }

}
