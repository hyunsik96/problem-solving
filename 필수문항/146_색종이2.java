import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[][] graph = new boolean[102][102];
        StringTokenizer st;
        while (N-- > 0) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for (int i = 1; i < 11; i++) {
                for (int j = 1; j < 11; j++) {
                    graph[x + i][y + j] = true;
                }
            }
        }
        int ans = 0;
        for (int a = 1; a < 102; a++) {
            for (int b = 1; b < 102; b++) {
                if (graph[a][b] != graph[a - 1][b]) {
                    ans++;
                }
                if (graph[a][b] != graph[a][b - 1]) {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
