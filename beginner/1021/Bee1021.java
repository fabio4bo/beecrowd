/*
* BEE 1021 - Banknotes and Coins - Level 6 - Beginner
*/

// Submission: 26/10/17, 4:38:59 PM

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1021 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        double money;

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        money = Double.parseDouble(br.readLine());

        System.out.printf("NOTAS:\n");
        System.out.printf(((int) money / 100) + " nota(s) de R$ 100.00\n");
        double cedula = money % 100;
        System.out.printf(((int) cedula / 50) + " nota(s) de R$ 50.00\n");
        cedula = cedula % 50;
        System.out.printf(((int) cedula / 20) + " nota(s) de R$ 20.00\n");
        cedula = cedula % 20;
        System.out.printf(((int) cedula / 10) + " nota(s) de R$ 10.00\n");
        cedula = cedula % 10;
        System.out.printf(((int) cedula / 5) + " nota(s) de R$ 5.00\n");
        cedula = cedula % 5;
        System.out.printf(((int) cedula / 2) + " nota(s) de R$ 2.00\n");
        cedula = cedula % 2;

        System.out.printf("MOEDAS:\n");
        System.out.printf(((int) cedula / 1) + " moeda(s) de R$ 1.00\n");

        cedula = cedula % 1;
        int moeda = (int) (cedula * 100);

        System.out.printf((moeda / 50) + " moeda(s) de R$ 0.50\n");
        moeda = moeda % 50;
        System.out.printf((moeda / 25) + " moeda(s) de R$ 0.25\n");
        moeda = moeda % 25;
        System.out.printf((moeda / 10) + " moeda(s) de R$ 0.10\n");
        moeda = moeda % 10;
        System.out.printf((moeda / 5) + " moeda(s) de R$ 0.05\n");
        moeda = moeda % 5;
        System.out.printf((moeda) + " moeda(s) de R$ 0.01\n");

    }

}
