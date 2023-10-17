import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long x = 1;
        long y = 1;
        for (int i = 2; i <= N; i++) {
            x = x + y;
            y = x - y;
        }
        System.out.println((x + y) * 2);
    }
}