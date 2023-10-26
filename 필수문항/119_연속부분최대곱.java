import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        double[] dp = new double[N];
        dp[0] = Double.parseDouble(br.readLine());
        for (int i = 1; i < N; i++) {
            Double now = Double.parseDouble(br.readLine());
            dp[i] = dp[i - 1] * now > now ? dp[i - 1] * now : now;
        }
        System.out.printf("%.3f", Arrays.stream(dp).max().getAsDouble());
    }
}
