import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] L = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] J = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] dp = new int[100];

        for (int i = 0; i < N; i++) {
            for (int j = 99; j >= L[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - L[i]] + J[i]);
            }
        }
        System.out.println(dp[99]);
    }
}
