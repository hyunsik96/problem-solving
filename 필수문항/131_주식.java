import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] prices = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int max = 0;
            long ans = 0;
            for (int i = N - 1; i >= 0; i--) {
                if (prices[i] >= max) {
                    max = prices[i];
                } else {
                    ans += max - prices[i];
                }
            }
            System.out.println(ans);
        }
    }
}
