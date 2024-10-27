
/*
* BEE 1018 - Banknotes - Level 4 - Beginner
*/
// Submission: 20/06/17, 6:21 PM

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1018 {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        int num, cem, aux, cinquenta, vinte, dez, cinco, dois, um;
        num = Integer.parseInt(in.readLine());
        cem = num / 100;
        aux = num % 100;
        cinquenta = (aux) / 50;
        aux %= 50;
        vinte = aux / 20;
        aux %= 20;
        dez = aux / 10;
        aux %= 10;
        cinco = aux / 5;
        aux %= 5;
        dois = aux / 2;
        aux %= 2;
        um = aux;

        System.out.printf(num + "\n" + cem + " nota(s) de R$ 100,00\n" + cinquenta + " nota(s) de R$ 50,00\n"
                + vinte + " nota(s) de R$ 20,00\n" + dez + " nota(s) de R$ 10,00\n" + cinco + " nota(s) de R$ 5,00\n"
                + dois + " nota(s) de R$ 2,00\n" + um + " nota(s) de R$ 1,00\n");

    }

}
