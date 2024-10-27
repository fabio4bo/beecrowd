/*
* BEE 1161 - Factorial Sum - Level 5 - Mathematics
*/

// Submission: 31/10/17, 7:18:01 PM 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1161 {

    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
//		System.out.println(fat(5));
        String nS;
        String[]vS = new String[2];
        
        while((nS = br.readLine())!=null) {
            vS=null;
            vS = nS.split(" ");
            System.out.print(fat(Long.parseLong(vS[0]))+ fat(Long.parseLong(vS[1]))+"\n");
        }		
    }
    
    public static long fat(long n)
    {
        if(n == 0) {
            return 1;
        }else
            return (n * fat(n - 1));
    }

}
