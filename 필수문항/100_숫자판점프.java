import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static int[] dx = { 1, -1, 0, 0 };
    public static int[] dy = { 0, 0, 1, -1 };
    public static int[][] graph = new int[5][5];
    public static Set<Integer> ans = new HashSet<>();

    public static void dfs(int x, int y, int jump, int num) {
        num += graph[x][y] * Math.pow(10, 5 - jump);
        if (jump == 5) {
            ans.add(num);
            num -= graph[x][y] * Math.pow(10, 5 - jump);
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (0 <= x + dx[i] && x + dx[i] < 5 && 0 <= y + dy[i] && y + dy[i] < 5) {
                dfs(x + dx[i], y + dy[i], jump + 1, num);
            }
        }
        num -= graph[x][y] * Math.pow(10, 5 - jump);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int x = 0; x < 5; x++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int y = 0; y < 5; y++) {
                graph[x][y] = Integer.parseInt(st.nextToken());
            }
        }

        for (int x = 0; x < 5; x++) {
            for (int y = 0; y < 5; y++) {
                dfs(x, y, 0, 0);
            }
        }
        System.out.println(ans.size());
    }
}