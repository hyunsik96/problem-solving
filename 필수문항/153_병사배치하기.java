import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] s = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            s[i] = Integer.parseInt(st.nextToken());
            dp[i] = i;
        }
        dp[n] = n;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[i] > dp[j] + i - j - 1 && s[i] < s[j]) {
                    dp[i] = dp[j] + i - j - 1;
                }
            }
        }
        System.out.println(dp[n]);
    }
}
