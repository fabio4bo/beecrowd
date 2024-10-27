/*
* BEE 1168 - LED - Level 3 - Strings
*/

// Submission: 01/10/18, 6:24:28 PM

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1168 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(in.readLine());
        String str = "";
        int cont = 0, aux;
        for (int i = 0; i < N; i++) {
            cont = 0;
            str = in.readLine();
            for (int j = 0; j < str.length(); j++) {
                // aux = Integer.parseInt(str.substring(j, j+1));
                aux = Integer.parseInt(String.valueOf(str.charAt(j)));
                if (aux == 1)
                    cont += 2;
                if (aux == 2 || aux == 3 || aux == 5)
                    cont += 5;
                if (aux == 4)
                    cont += 4;
                if (aux == 6 || aux == 9 || aux == 0)
                    cont += 6;
                if (aux == 7)
                    cont += 3;
                if (aux == 8)
                    cont += 7;
            }
            System.out.println(cont + " leds");
        }

    }

}
