/*
* BEE 1024 - Encryption - Level 5 - Strings
*/

// Submission: 28/09/18, 5:30 PM

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1024 {

    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);
        
        int N = Integer.parseInt(in.readLine());
        String string  = "";

        for(int i = 0; i < N; i++) {
            string = in.readLine();
            System.out.println(criptografia(string));
        }


    }
    static String criptografia(String string) {
        string = first(string);
        string = second(string);
        string = third(string);
        return string;
    }
    static String first(String string) {
        String aux = "";
        for(int i = 0; i < string.length(); i++) {
            if((string.charAt(i) >= 'a' && string.charAt(i) <= 'z') 
                    || (string.charAt(i) >= 'A' && string.charAt(i) <= 'Z')){
                aux += (char)(string.charAt(i)+3);
            }else {
                aux+= (char)(string.charAt(i));
            }
        }
        return aux;
    }
    static String second(String string) {
        String temp = "";
        for(int c=string.length()-1; c>=0; c--)
        {
            temp = temp+(char)(string.charAt(c));
        }
        return temp;
    }
    static String third(String string) {
        String aux = "";
        for(int i = 0; i < string.length(); i++) {
            if(i >= (string.length()/2))
                aux += (char)(string.charAt(i)-1);
            else
                aux += (char)(string.charAt(i));
        }
        return aux;
    }

}
