import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<int[]> sharks = new ArrayList<>();
        for (int x = 0; x < N; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < M; y++) {
                if (st.nextToken().equals("1")) {
                    sharks.add(new int[] { x, y });
                }
            }
        }
        int[][] graph = new int[N][M];
        int maxLine = Math.max(N, M);
        for (int i = 0; i < N; i++) {
            Arrays.fill(graph[i], maxLine - 1);
        }

        int[] dx = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] dy = { -1, 0, 1, -1, 1, -1, 0, 1 };

        for (int[] shark : sharks) {
            Queue<int[]> que = new ArrayDeque<>();
            que.add(shark);
            graph[shark[0]][shark[1]] = 0;
            while (que.size() != 0) {
                int[] xy = que.poll();
                for (int i = 0; i < 8; i++) {
                    if (0 <= xy[0] + dx[i] &&
                            xy[0] + dx[i] < N &&
                            0 <= xy[1] + dy[i] &&
                            xy[1] + dy[i] < M &&
                            graph[xy[0] + dx[i]][xy[1] + dy[i]] > graph[xy[0]][xy[1]] + 1) {
                        graph[xy[0] + dx[i]][xy[1] + dy[i]] = graph[xy[0]][xy[1]] + 1;
                        que.add(new int[] { xy[0] + dx[i], xy[1] + dy[i] });
                    }
                }
            }
        }
        int ans = 0;
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                ans = Math.max(ans, graph[x][y]);
            }
        }
        System.out.println(ans);
    }
}
