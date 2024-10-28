/*
* BEE 1047 - Game Time with Minutes - Level 9 - Beginner
*/

import java.util.Scanner;

public class Bee1047 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int initialHour = in.nextInt();
        int initialMinute = in.nextInt();
        int finalHour = in.nextInt();
        int finalMinute =  in.nextInt();
        in.close();

        int resultHour = (24 - initialHour) - (24 - finalHour);
        int resultMinute = (finalMinute - initialMinute) % 60; // % is different in python?
        
        if (resultMinute < 0) // in python is not necessary
            resultMinute += 60;

        if (resultHour == 0 && resultMinute == 0)
            resultHour = 24;
        if ((60 - initialMinute + finalMinute) / 60 == 0)
            resultHour -= 1;
        if (resultHour < 0)
            resultHour += 24;


        System.out.println("O JOGO DUROU "+ resultHour +" HORA(S) E "+ resultMinute +" MINUTO(S)");
    }
}