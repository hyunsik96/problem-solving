import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        boolean[][] visited = new boolean[R][C];
        String[] graph = new String[R];
        for (int i = 0; i < R; i++) {
            graph[i] = br.readLine();
        }
        int k = 0;
        int v = 0;
        int[] kv = new int[2];
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };

        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if (!visited[x][y] && graph[x].charAt(y) != '#') {
                    Arrays.fill(kv, 0);
                    Queue<Integer[]> que = new ArrayDeque<>();
                    que.add(new Integer[] { x, y });
                    visited[x][y] = true;
                    if (graph[x].charAt(y) != '.') {
                        kv[graph[x].charAt(y) == 'k' ? 0 : 1]++;
                    }
                    while (!que.isEmpty()) {
                        Integer[] p = que.poll();
                        for (int i = 0; i < 4; i++) {
                            if (0 <= p[0] + dx[i] &&
                                    p[0] + dx[i] < R &&
                                    0 <= p[1] + dy[i] &&
                                    p[1] + dy[i] < C &&
                                    !visited[p[0] + dx[i]][p[1] + dy[i]] &&
                                    graph[p[0] + dx[i]].charAt(p[1] + dy[i]) != '#') {
                                if (graph[p[0] + dx[i]].charAt(p[1] + dy[i]) != '.') {
                                    kv[graph[p[0] + dx[i]].charAt(p[1] + dy[i]) == 'k' ? 0 : 1]++;
                                }
                                visited[p[0] + dx[i]][p[1] + dy[i]] = true;
                                que.add(new Integer[] { p[0] + dx[i], p[1] + dy[i] });
                            }
                        }
                    }
                    if (kv[0] > kv[1]) {
                        k += kv[0];
                    } else {
                        v += kv[1];
                    }
                }
            }
        }
        System.out.printf("%d %d", k, v);
    }
}
