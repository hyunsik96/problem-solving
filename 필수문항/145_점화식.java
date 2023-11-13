import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] dp = new long[36];
        dp[0] = 1;
        // 0 * i-1 ~ i-1 * 0
        for (int i = 1; i < 36; i++) {
            for (int l = 0; l < i; l++) {
                dp[i] += dp[l] * dp[i - l - 1];
            }
        }
        System.out.println(dp[N]);
    }
}
