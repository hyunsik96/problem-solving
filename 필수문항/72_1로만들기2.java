import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N + 1];

        int tmpMin = 0;
        for (int i = 2; i < N + 1; i++) {
            tmpMin = dp[i - 1];
            if (i % 2 == 0 && tmpMin > dp[i / 2]) {
                tmpMin = dp[i / 2];
            }
            if (i % 3 == 0 && tmpMin > dp[i / 3]) {
                tmpMin = dp[i / 3];
            }
            dp[i] = tmpMin + 1;
        }

        ans.append(dp[N]).append("\n").append(N);

        int tmpN = 0;
        while (N != 1) {
            tmpMin = dp[N - 1];
            tmpN = N - 1;
            if (N % 2 == 0 && tmpMin > dp[N / 2]) {
                tmpMin = dp[N / 2];
                tmpN = N / 2;
            }
            if (N % 3 == 0 && tmpMin > dp[N / 3]) {
                tmpMin = dp[N / 3];
                tmpN = N / 3;
            }
            N = tmpN;
            ans.append(" ").append(N);
        }
        System.out.println(ans);
    }
}