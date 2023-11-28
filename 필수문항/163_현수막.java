import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[][] graph = new int[M][N];
        boolean[][] visited = new boolean[M][N];
        for (int x = 0; x < M; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < N; y++) {
                graph[x][y] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        int[] dx = { -1, 0, 1, -1, 1, -1, 0, 1 };
        int[] dy = { -1, -1, -1, 0, 0, 1, 1, 1 };
        for (int ox = 0; ox < M; ox++) {
            for (int oy = 0; oy < N; oy++) {
                if (graph[ox][oy] == 1 && !visited[ox][oy]) {
                    answer++;
                    Queue<Integer[]> queue = new ArrayDeque<>();
                    queue.add(new Integer[] { ox, oy });
                    while (queue.size() != 0) {
                        Integer[] tmp = queue.poll();
                        int x = tmp[0];
                        int y = tmp[1];
                        for (int i = 0; i < 8; i++) {
                            if (0 <= x + dx[i] && x + dx[i] < M &&
                                    0 <= y + dy[i] && y + dy[i] < N &&
                                    !visited[x + dx[i]][y + dy[i]] &&
                                    graph[x + dx[i]][y + dy[i]] == 1) {
                                visited[x + dx[i]][y + dy[i]] = true;
                                queue.add(new Integer[] { x + dx[i], y + dy[i] });
                            }
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
