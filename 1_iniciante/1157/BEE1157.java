// 
// BEE 1157 - Divisores I - Nível 1 - Iniciante
// 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BEE1157 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        int N = Integer.parseInt(in.readLine());
        divisores(N);
    }

    public static void divisores(int N){
        for(int i=1; i <= N; i++){
            if(N%i == 0)
                System.out.println(i);
        }
    }

}
