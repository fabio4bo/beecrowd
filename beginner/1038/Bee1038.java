/*
* BEE 1038 - Snack - Level 1 - Beginner
*/

// Submission: 28/10/17, 9:37:25 PM

import java.util.Scanner;

public class Bee1038 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int CQ = 4;// 1
        final double XSal = 4.5;// 2
        final int XBac = 5;// 3
        final int Tor = 2;// 4
        final double Refri = 1.5;// 5
        int codigo = entrada.nextInt();
        int quantidade = entrada.nextInt();

        switch (codigo) {
            case 1:
                System.out.printf("Total: R$ %.2f\n", (CQ * (double) quantidade));
                break;
            case 2:
                System.out.printf("Total: R$ %.2f\n", XSal * (double) quantidade);
                break;
            case 3:
                System.out.printf("Total: R$ %.2f\n", (XBac * (double) quantidade));
                break;
            case 4:
                System.out.printf("Total: R$ %.2f\n", Tor * (double) quantidade);
                break;
            case 5:
                System.out.printf("Total: R$ %.2f\n", Refri * (double) quantidade);
                break;
            default:
                break;
        }

    }

}
