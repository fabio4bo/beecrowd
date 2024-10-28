/*
* BEE 1042 - Simple Sort - Level 2 - Beginner
*/

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Bee1042 {

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        while (in.hasNextInt()) {
            numbers.add(in.nextInt());
        }
        in.close();

        ArrayList<Integer> originalSort = new ArrayList<Integer>();
        for (int i : numbers)
            originalSort.add(i);

        Collections.sort(numbers);

        for (int n : numbers) {
            System.out.println(n);
        }
        System.out.println();

        for (int n : originalSort) {
            System.out.println(n);
        }

    }
}
