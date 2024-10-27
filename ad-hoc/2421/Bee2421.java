/*
* BEE 2421 - Álbum de Fotos - Level 8 - Ad-hoc
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Bee2421 {

    public static void main(String[] args) {
        int x, y, l0, h0, l1, h1;
        Scanner entrada = new Scanner(System.in);
        ArrayList<Integer> intNumbers = new ArrayList<Integer>();
        intNumbers = inputToInt();

        x = intNumbers.get(0);
        y = intNumbers.get(1);
        l0 = intNumbers.get(2);
        h0 = intNumbers.get(3);
        l1 = intNumbers.get(4);
        h1 = intNumbers.get(5);

        if ((l0 + l1 <= x && max(h0, h1) <= y) ||
                (l0 + h1 <= x && max(h0, l1) <= y) ||
                (l0 + l1 <= y && max(h0, h1) <= x) ||
                (l0 + h1 <= y && max(h0, l1) <= x) ||
                (max(l0, l1) <= x && h0 + h1 <= y) ||
                (max(l0, h1) <= x && h0 + l1 <= y) ||
                (max(l0, l1) <= y && h0 + h1 <= x) ||
                (max(l0, h1) <= y && h0 + l1 <= x))
            System.out.println("S");
        else
            System.out.println("N");

        entrada.close();
    }

    public static ArrayList<Integer> inputToInt() {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> intNumbers = new ArrayList<Integer>();
        String[] s = new String[2];

        while (in.hasNextLine()) {
            s = in.nextLine().split(" ");
            intNumbers.add(Integer.parseInt(s[0]));
            intNumbers.add(Integer.parseInt(s[1]));
        }
        in.close();
        return intNumbers;
    }

    public static int max(int n1, int n2) {
        int maior = n1;

        if (maior < n2)
            maior = n2;

        return maior;
    }
}
