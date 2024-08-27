/**
 * BEE 1161 - Soma de Fatoriais - Nível 5 - Matemática
 */
import java.io.*;
public class BEE1161 {
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        String numbers;

        while ((numbers = in.readLine()) != null) {
            int M = Integer.parseInt(numbers.split(" ")[0]);
            int N = Integer.parseInt(numbers.split(" ")[1]);

            System.out.println(fatorial(M) + fatorial(N));
        }
    }

    public static long fatorial(int N) {
        if (N == 0)
            return 1;
        return N * fatorial(N - 1);
    }
}
