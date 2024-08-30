/*
 * BEE 1065 - Pares entre Cinco Números - Nível 1 - Iniciante
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1065 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int pares = 0;
        for (int i = 0; i < 5; i++) {
            if (Integer.parseInt(in.readLine()) % 2 == 0)
                pares++;
        }
        System.out.println(pares + " valores pares");
    }
}
