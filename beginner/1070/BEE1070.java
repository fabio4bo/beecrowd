/*
 * BEE 1070 - Seis Números Ímpares - Level 1 - Beginner
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1070 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int X = Integer.parseInt(in.readLine());

        if (X % 2 == 0)
            X++;

        for (int i = 0; i < 12; i+=2) {
            System.out.println(X + i);
        }

    }
}
