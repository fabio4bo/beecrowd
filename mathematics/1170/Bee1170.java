/*
* BEE 1170 - Blobs - Level 3 - Mathematics
*/

import java.util.Scanner;

public class Bee1170 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double c;
        int n = in.nextInt();
        for(int i = 0; i < n; i++){
            c = in.nextDouble();

            System.out.println(log2n(c) + " dias");
        }
        in.close();
    }
    public static int result(double c){
        int count = 0;

        while(c > 1){
            c /= 2;
            count++;
        }
        return count;
    }
    public static int log2n(double c){
        return (int) Math.ceil(Math.log(c) / Math.log(2));
    }
}