import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[][] graph;
    private static int[][] price;
    private static int[][] now = new int[2][2];
    private static int ans = 200 * 100;

    private static int getPrice(int x, int y) {
        return graph[x - 1][y] + graph[x][y - 1] + graph[x][y] + graph[x + 1][y] + graph[x][y + 1];
    }

    private static boolean checkNow(int x, int y, int num) {
        for (int i = 0; i < num; i++) {
            if (Math.abs(now[i][0] - x) + Math.abs(now[i][1] - y) < 3) {
                return false;
            }
        }
        return true;
    }

    private static void dfs(int x, int y, int num, int nowPrice) {
        if (num == 1) {
            now[0][0] = x;
            now[0][1] = y;
        } else if (num == 2) {
            now[1][0] = x;
            now[1][1] = y;
        } else {
            if (ans > nowPrice) {
                ans = nowPrice;
            }
            return;
        }
        for (int nx = x; nx <= N - 2; nx++) {
            for (int ny = 1; ny <= N - 2; ny++) {
                if (checkNow(nx, ny, num)) {
                    dfs(nx, ny, num + 1, nowPrice + price[nx][ny]);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        price = new int[N][N];
        StringTokenizer st;

        for (int x = 0; x < N; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < N; y++) {
                graph[x][y] = Integer.parseInt(st.nextToken());
            }
        }

        for (int x = 1; x <= N - 2; x++) {
            for (int y = 1; y <= N - 2; y++) {
                price[x][y] = getPrice(x, y);
            }
        }

        for (int x = 1; x <= N - 2; x++) {
            for (int y = 1; y <= N - 2; y++) {
                dfs(x, y, 1, price[x][y]);
            }
        }

        System.out.println(ans);

    }
}
