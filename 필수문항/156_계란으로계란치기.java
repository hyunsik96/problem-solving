import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int n;
    private static int[][] eggs;
    private static int ans;

    private static void dfs(int idx) {
        if (idx == n) {
            int broken = 0;
            for (int[] egg : eggs) {
                if (egg[0] <= 0) {
                    broken++;
                }
            }
            ans = Math.max(ans, broken);
        } else if (eggs[idx][0] <= 0) {
            dfs(idx + 1);
        } else {
            boolean check = false;
            for (int i = 0; i < n; i++) {
                if (i == idx) {
                    continue;
                } else if (eggs[i][0] > 0) {
                    check = true;
                    eggs[i][0] -= eggs[idx][1];
                    eggs[idx][0] -= eggs[i][1];
                    dfs(idx + 1);
                    eggs[i][0] += eggs[idx][1];
                    eggs[idx][0] += eggs[i][1];
                }
            }
            if (!check) {
                dfs(idx + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        eggs = new int[n][2];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            eggs[i][0] = Integer.parseInt(st.nextToken());
            eggs[i][1] = Integer.parseInt(st.nextToken());
        }
        dfs(0);
        System.out.println(ans);
    }
}
