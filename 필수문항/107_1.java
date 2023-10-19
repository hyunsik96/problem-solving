import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class App {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] dp = new int[10001];
        for (int i = 1; i < 10001; i++) {
            if (i % 2 != 0 && i % 5 != 0) {
                int ans = 1;
                int num = 1;
                while (num % i != 0) {
                    num = (num % i) * 10 + 1;
                    ans++;
                }
                dp[i] = ans;
            }
        }

        while (true) {
            try {
                System.out.println(dp[Integer.parseInt(br.readLine())]);
            } catch (Exception e) {
                break;
            }
        }
    }
}
