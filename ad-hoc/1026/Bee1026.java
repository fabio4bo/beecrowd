/*
* BEE 1026 - To Carry or not to Carry - Level 5 - Ad-hoc
*/

import java.io.IOException;
import java.math.BigInteger;
import java.util.Scanner;

public class Bee1026 {

    public static void main(String[] args) throws IOException, NullPointerException {
        Scanner in = new Scanner(System.in);

        String[] numbers;
        while (in.hasNext()) {
            numbers = in.nextLine().split(" ");
            BigInteger X = new BigInteger(numbers[0]);
            BigInteger Y = new BigInteger(numbers[1]);

            System.out.println(X.xor(Y));// ou long com ^
        in.close(); //com isso deu Time limit exceeded
        }
    }
}