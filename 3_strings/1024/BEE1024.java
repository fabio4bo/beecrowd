/*
 * BEE 1024 - Criptografia - Nível 5 - Strings
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1024 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int N = Integer.parseInt(in.readLine());

        for (int i = 0; i < N; i++) {
            char[] texto = in.readLine().trim().toCharArray();
            int tamanho = texto.length;
            for (int j = 0; j < tamanho; j++) {
                if (Character.isAlphabetic(texto[j]))
                    texto[j] += 3;
            }

            for (int j = 0; j < tamanho / 2; j++) {
                char aux = texto[j];
                texto[j] = texto[tamanho - j - 1];
                texto[tamanho - j - 1] = aux;
            }

            for (int j = texto.length / 2; j < texto.length; j++) {
                texto[j] -= 1;
            }

            System.out.println(texto);
        }

    }
}