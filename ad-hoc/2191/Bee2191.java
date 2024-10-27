/*
* BEE 2191 - Goal Difference - Level 8 - Ad-hoc
*/

import java.io.IOException;
import java.util.Scanner;

public class Bee2191 {

    public static void main(String[] args) throws IOException {
        int testes = 0, x, y, n, primeiro, prim_temp, ultimo, s_atual, s_maior;
        String[] numbers;
        int[] numbersInt;
        Scanner in = new Scanner(System.in);

        while (in.hasNextLine()) {
            n = Integer.parseInt(in.nextLine());

            if (n == 0) {
                in.close();
                break;
            }

            testes++;
            primeiro = 0;
            ultimo = 0;
            prim_temp = 0;
            s_maior = -1;
            s_atual = 0;

            for (int i = 0; i < n; i++) {
                numbers = in.nextLine().split(" ");

                numbersInt = toInt(numbers);

                x = numbersInt[0];
                y = numbersInt[1];

                s_atual += x - y;

                if (s_atual < 0) {
                    prim_temp = i + 1;
                    s_atual = 0;
                }

                if (s_atual >= s_maior) {
                    s_maior = s_atual;
                    primeiro = prim_temp;
                    ultimo = i;
                }
            }
            System.out.println("Teste " + testes);
            if (s_maior > 0)
                System.out.println((primeiro + 1) + " " + (ultimo + 1) + "\n");
            else
                System.out.println("nenhum\n");

        }
    }

    public static int[] toInt(String[] numbers) {
        int[] intNumbers = new int[2];

        intNumbers[0] = Integer.parseInt(numbers[0]);
        intNumbers[1] = Integer.parseInt(numbers[1]);

        return intNumbers;
    }
}