/*
 * BEE 1019 - Conversão de Tempo - Nível 1 - Iniciante
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1019 {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        int N = Integer.parseInt(in.readLine());

        int hora = N / 3600;
        int minute = (N % 3600) / 60;
        int seconds = N % 60;

        System.out.println(hora + ":" + minute + ":" + seconds);
    }

}