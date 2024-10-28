/*
* BEE 1041 - Coordinates of a Point - Level 3 - Beginner
*/

// Submission: 31/10/17, 7:53 PM

import java.util.Scanner;

public class Bee1041 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double x,y;
        x = entrada.nextDouble();
        y = entrada.nextDouble();
        entrada.close();
        
        if(x == 0.0 && y == 0.0){
            System.out.println("Origem");
        }else if(x>0.0 && y>0.0){
            System.out.println("Q1");
        }else if(x!=0 && y == 0){
            System.out.println("Eixo X");
        }else if(x == 0 && y!=0){
            System.out.println("Eixo Y");
        }else if(x > 0 && y < 0){
            System.out.println("Q4");
        }else if(x < 0 && y < 0){
            System.out.println("Q3");
        }else if(x < 0 && y > 0){
            System.out.println("Q2");
        }
        
    }

}
