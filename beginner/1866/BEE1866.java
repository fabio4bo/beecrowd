/*
 * BEE 1866 - Conta - Level 1 - Beginner
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1866 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int C = (Integer.parseInt(in.readLine()));

        for (int i = 0; i < C; i++) {
            int N = Integer.parseInt(in.readLine());
            System.out.println(N%2);
        }
    }
}
