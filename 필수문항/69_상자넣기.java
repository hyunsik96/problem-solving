import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] boxes = new int[n];
        for (int i = 0; i < n; i++) {
            boxes[i] = Integer.parseInt(st.nextToken());
        }
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 0; i < n; i++) {
            int tmpMax = 0;
            for (int m = 0; m < i; m++) {
                if (boxes[m] < boxes[i] && dp[m] > tmpMax) {
                    tmpMax = dp[m];
                }
            }
            dp[i] = tmpMax + 1;
            if (dp[i] > ans) {
                ans = dp[i];
            }
        }
        System.out.println(ans);
    }
}
