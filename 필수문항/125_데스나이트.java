import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int fx = Integer.parseInt(st.nextToken());
        int fy = Integer.parseInt(st.nextToken());
        int tx = Integer.parseInt(st.nextToken());
        int ty = Integer.parseInt(st.nextToken());
        int[] dx = { -2, -2, 0, 0, 2, 2 };
        int[] dy = { -1, 1, -2, 2, -1, 1 };
        boolean[][] visited = new boolean[N][N];
        visited[fx][fy] = true;

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(fx);
        queue.add(fy);
        queue.add(0);

        while (queue.size() > 0) {
            int x = queue.poll();
            int y = queue.poll();
            int count = queue.poll();
            for (int i = 0; i < 6; i++) {
                if (0 <= x + dx[i] && x + dx[i] < N && 0 <= y + dy[i] && y + dy[i] < N
                        && !visited[x + dx[i]][y + dy[i]]) {
                    if (x + dx[i] == tx && y + dy[i] == ty) {
                        System.out.println(count + 1);
                        return;
                    }
                    visited[x + dx[i]][y + dy[i]] = true;
                    queue.add(x + dx[i]);
                    queue.add(y + dy[i]);
                    queue.add(count + 1);
                }
            }
        }
        System.out.println(-1);
    }
}
