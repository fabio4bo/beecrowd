import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * BEE 2880
 */
public class BEE2880 {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        char[] menCifrada = in.readLine().trim().toCharArray();
        char[] crib = in.readLine().trim().toCharArray();

        int T = menCifrada.length;
        int C = crib.length;
        int cont = 0;

        for(int i = 0; i < T-C+1; i++){
            boolean confere = false;
            char[] temp = Arrays.copyOfRange(menCifrada, i, C+i);
            for(int j = 0; j < C; j++){
                if(temp[j] == crib[j])
                    confere = true;
            }
            if(!confere)
                cont++;
        }
        System.out.println(cont);
    }
    
}