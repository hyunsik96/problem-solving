import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[][] graph = new int[M][N];
        ArrayDeque<int[]> deque = new ArrayDeque<>();
        String line = br.readLine();
        for (int y = 0; y < N; y++) {
            graph[0][y] = line.charAt(y) - 48;
            if (graph[0][y] == 0) {
                deque.add(new int[] { 0, y });
                graph[0][y] = 1;
            }
        }
        for (int x = 1; x < M; x++) {
            line = br.readLine();
            for (int y = 0; y < N; y++) {
                graph[x][y] = line.charAt(y) - 48;
            }
        }

        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };

        while (!deque.isEmpty()) {
            int[] xy = deque.pollFirst();
            for (int i = 0; i < 4; i++) {
                if (0 <= xy[0] + dx[i] &&
                        xy[0] + dx[i] < M &&
                        0 <= xy[1] + dy[i] &&
                        xy[1] + dy[i] < N &&
                        graph[xy[0] + dx[i]][xy[1] + dy[i]] == 0) {
                    if (xy[0] + dx[i] == M - 1) {
                        System.out.println("YES");
                        return;
                    }
                    graph[xy[0] + dx[i]][xy[1] + dy[i]] = 1;
                    deque.add(new int[] { xy[0] + dx[i], xy[1] + dy[i] });
                }
            }
        }
        System.out.println("NO");
    }
}
