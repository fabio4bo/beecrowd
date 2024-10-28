/*A is needed in B for the solution 1279
* BEE 1279 - Leap Year or Not Leap Year and … - Level 6 - Mathematics
*/

import java.math.BigInteger;
import java.util.Scanner;

public class Bee1279 {

    public static BigInteger ZERO = BigInteger.ZERO;
    public static boolean flag = false;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger year;
        while (in.hasNextBigInteger()) {
            year = in.nextBigInteger();
            result(year);
        }
        in.close();
    }

    public static void result(BigInteger year) {
        if (flag)
            System.out.println();
        if (isLeap(year))
            System.out.println("This is leap year.");
        if (isHuluculu(year))
            System.out.println("This is huluculu festival year.");
        if (isBulukulu(year))
            System.out.println("This is bulukulu festival year.");
        if (!isLeap(year) && !isHuluculu(year) && !isBulukulu(year))
            System.out.println("This is an ordinary year.");
        flag = true;
    }

    public static boolean isLeap(BigInteger year) {
        if (year.mod(new BigInteger("4")).equals(ZERO) && !(year.mod(new BigInteger("100")).equals(ZERO)))
            return true;
        else if (year.mod(new BigInteger("100")).equals(ZERO) && year.mod(new BigInteger("400")).equals(ZERO))
            return true;
        else
            return false;
    }

    public static boolean isHuluculu(BigInteger year) {
        return (year.mod(new BigInteger("15")).equals(ZERO));
    }

    public static boolean isBulukulu(BigInteger year) {
        return (year.mod(new BigInteger("55")).equals(ZERO)) && isLeap(year);
    }
}