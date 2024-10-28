/*
* BEE 1279 - Leap Year or Not Leap Year and … - Level 6 - Mathematics
*/

import java.util.Scanner;

public class Bee1279 {

    public static boolean flag = false;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String year;
        long newYear;
        while(in.hasNextLine()){
            year = in.nextLine();
            if (year.length() >= 18){
                newYear = Long.parseLong(year.substring(year.length() - 19, year.length()));
            }else{
                newYear = Long.parseLong(year);
            }
            result(newYear);
        }
        in.close();
    }

    public static void result(long year) {
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

    public static boolean isLeap(long year) {
        if (year % 4 == 0 && !(year % 100 == 0))
            return true;
        else if (year % 100 == 0 && year % 400 == 0)
            return true;
        else
            return false;
    }

    public static boolean isHuluculu(long year) {
        return (year % 15 == 0);
    }

    public static boolean isBulukulu(long year) {
        return (year % 55 == 0) && isLeap(year);
    }
}