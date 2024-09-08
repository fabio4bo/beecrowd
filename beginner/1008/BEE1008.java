/* 
 * BEE 1008 - Salário - Level 2 - Beginner
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1008 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int numero = Integer.parseInt(in.readLine());
        int horasTrabalhadas = Integer.parseInt(in.readLine());
        float valorHora = Float.parseFloat(in.readLine());

        System.out.println(String.format("NUMBER = %d", numero));
        System.out.println(String.format("SALARY = U$ %.2f", horasTrabalhadas * valorHora));

    }
}
