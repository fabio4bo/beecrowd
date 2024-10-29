/*
* BEE 1212 - Primary Arithmetic - Level 8 - Mathematics
*/

import java.util.Scanner;

public class Bee1212 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long x, y;
        while (in.hasNextLong()) {
            x = in.nextLong();
            y = in.nextLong();
            if (x == 0 && y == 0)
                break;
            result(x, y);

        }
        in.close();
    }

    public static void result(long x, long y) {
        int count = 0;
        int aux = 0;
        String texto;

        while (x != 0 || y != 0) {
            if ((x % 10) + (y % 10) + aux > 9) {
                count++;
                aux = 1;
            } else
                aux = 0;
            x /= 10;
            y /= 10;
        }
        if (count == 0)
            texto = "No carry operation.";
        else if (count == 1)
            texto = "1 carry operation.";
        else
            texto = count + " carry operations.";

        System.out.println(texto);

    }
}