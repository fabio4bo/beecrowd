/*
* BEE 1169 - Grains in a Chess Board - Level 4 - Mathematics
*/

import java.math.BigInteger;
import java.util.Scanner;

public class Bee1169 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x;
        for(int i = 0; i < n; i++){
            x = in.nextInt();
            System.out.println(result(x) + " kg");
        }
        in.close();
    }
    public static BigInteger result(int n){
        BigInteger two = new BigInteger("2");
        BigInteger grains = two.pow(n);
        return grains.divide(new BigInteger("12000"));
    }
}