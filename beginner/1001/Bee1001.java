/*
* BEE 1001 - Extremely Basic - Level 4 - Beginner
*/

// Submission: 31/05/17, 7:59:35 PM

import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT:
 * O nome da classe deve ser "Main" para que a sua solução execute
 * Class name must be "Main" for your solution to execute
 * El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Bee1001 {
    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);
        int A, B, X;
        A = entrada.nextInt();
        B = entrada.nextInt();
        entrada.close();
        
        X = A + B;
        System.out.println("X = " + X);
    }

}