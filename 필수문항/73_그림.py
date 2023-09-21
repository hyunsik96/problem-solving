import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    private static int[][] graph;
    private static int n;
    private static int m;

    private static void bfs() {

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        int tmpNum = 0;
        for (int x = 0; x < n; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < m; y++) {
                tmpNum = Integer.parseInt(st.nextToken());
                if (tmpNum == 1) {
                    graph[x][y] = 1;
                }
            }
        }

        int total = 0;
        int maxNum = 0;
        int checkMax = 0;
        Queue<int[]> queue;
        int[] tmpInt;
        int tmpX = 0, tmpY = 0;

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (graph[x][y] == 1) {
                    checkMax = 1;
                    total++;
                    queue = new ArrayDeque<>();
                    queue.add(new int[]{x, y});
                    graph[x][y] = 0;
                    while (!queue.isEmpty()) {
                        tmpInt = queue.remove();
                        tmpX = tmpInt[0];
                        tmpY = tmpInt[1];
                        for (int i = 0; i < 4; i++) {
                            if (0 <= tmpX + dx[i] && tmpX + dx[i] < n &&
                                    0 <= tmpY + dy[i] && tmpY + dy[i] < m &&
                                    graph[tmpX + dx[i]][tmpY + dy[i]] == 1) {
                                queue.add(new int[]{tmpX + dx[i], tmpY + dy[i]});
                                graph[tmpX + dx[i]][tmpY + dy[i]] = 0;
                                checkMax++;
                            }
                        }
                    }
                    if (checkMax > maxNum) {
                        maxNum = checkMax;
                    }
                }
            }
        }

        ans.append(total).append("\n").append(maxNum);
        System.out.println(ans);
    }
}


