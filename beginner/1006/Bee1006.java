/*
* BEE 1006 - Average 2 - Level 1 - Beginner
*/

// Submission: 07/06/17, 2:05:16 PM 
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Bee1006 {
 
    public static void main(String[] args) throws IOException {
 
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        
        double A, B, C, MED;
        
        A = 2 * Double.parseDouble(in.readLine());
        B = 3 * Double.parseDouble(in.readLine());
        C = 5 * Double.parseDouble(in.readLine());
        
        MED = (A + B + C)/10;
        String MEDIA = String.format("%.1f", MED);
        
        System.out.printf("MEDIA = "+MEDIA+"\n"); 
 
    }
 
}