import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static int N;
    public static int[] W;
    public static boolean[] visited;
    public static int ans;
    public static int num;

    public static void dfs(int energy) {
        if (num == 2) {
            ans = Math.max(ans, energy);
            return;
        }
        for (int i = 1; i < N - 1; i++) {
            if (!visited[i]) {
                num--;
                visited[i] = true;

                int lp = i - 1;
                int rp = i + 1;
                while (visited[lp]) {
                    lp--;
                }
                while (visited[rp]) {
                    rp++;
                }
                dfs(energy + W[lp] * W[rp]);

                visited[i] = false;
                num++;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        W = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        visited = new boolean[N];
        num = N;
        dfs(0);
        System.out.println(ans);
    }
}
