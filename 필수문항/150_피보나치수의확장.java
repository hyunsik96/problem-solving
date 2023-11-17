import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int fibo(int n) {
        int before = 0;
        int now = 1;
        int i = 1;
        while (i++ < n) {
            now = now + before;
            before = (now - before) % 1000000000;
            now %= 1000000000;
        }
        return now;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n > 0) {
            System.out.println(1);
            System.out.println(fibo(n));
        } else if (n < 0) {
            n *= -1;
            if (n % 2 == 1) {
                System.out.println(1);
            } else {
                System.out.println(-1);
            }
            System.out.println(fibo(n));
        } else {
            System.out.println(0);
            System.out.println(0);
        }
    }
}
