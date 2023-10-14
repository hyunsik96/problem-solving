import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        BigInteger[] dp = new BigInteger[31];
        dp[0] = BigInteger.valueOf(1);
        for (int i = 1; i < 31; i++) {
            dp[i] = dp[i - 1].multiply(BigInteger.valueOf(i));
        }

        int x = (K - 1) / M;
        int y = K - x * M - 1;

        if (K == 0) {
            x = 0;
            y = 0;
        }

        System.out.println((dp[x + y].divide(dp[x]).divide(dp[y]))
                .multiply(dp[N + M - 2 - x - y].divide(dp[N - 1 - x]).divide(dp[M - 1 - y])));
    }

}