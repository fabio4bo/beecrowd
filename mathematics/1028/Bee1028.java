import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee1028 {
    
    public static void main(String[] args) throws IOException {
        
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        
        int A, B, X;
        
        X = Integer.parseInt(in.readLine());
        
        for(int i = 0; i < X; i++){
            String str = in.readLine();
            String[] numbers = str.split(" ");

            A = Integer.parseInt(numbers[0]);
            B = Integer.parseInt(numbers[1]);

            System.out.println(MDC(A, B));
        }
    }
    public static Integer MDC(int A, int B){
        if(B == 0){
            return A;
        }
        return MDC(B, A % B);
    }
    
}
