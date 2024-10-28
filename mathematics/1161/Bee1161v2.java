import java.io.*;
import java.math.BigInteger;

/**
 * Bee1161 - Soma de Fatoriais
 */
public class Bee1161v2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        String numbers;

        while ((numbers = in.readLine()) != null) {
            int n1 = Integer.parseInt(numbers.split(" ")[0]);
            int n2 = Integer.parseInt(numbers.split(" ")[1]);

            BigInteger fatorialN1 = fatorial(n1);
            BigInteger fatorialN2 = fatorial(n2);

            BigInteger sum = fatorialN1.add(fatorialN2);

            System.out.println(sum);
        }
    }

    // jeito simples não funciona com números grandes
    public static BigInteger fatorial(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 1; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }
}
