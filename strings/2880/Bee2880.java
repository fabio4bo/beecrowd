/*
* BEE 2880 - Enigma - Level 4 - Strings
*/

// Submission: 19/09/18, 2:49:26 PM

import java.util.Scanner;

public class Bee2880 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        String f1 = in.nextLine();
        String f2 = in.nextLine();
        int t1 = f1.length();
        int t2 = f2.length();
        int cont = 0;
        
//		FDMLCRDMRALF
//		ARMADA
        String sub = "";
        boolean bool = false;

        for(int i = 0; i < (t1-t2+1); i++) {
            bool = false;
            sub = f1.substring(i, t2+i);
            for(int j = 0; j < t2; j++) {
                if(f2.charAt(j) == sub.charAt(j))
                    bool = true;
            }
            if(bool==false)
                cont++;
        }
        System.out.println(cont);
    }

}
