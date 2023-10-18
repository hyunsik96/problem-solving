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
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        String[] graph = new String[R];
        boolean[][] visited = new boolean[R][C];
        for (int i = 0; i < R; i++) {
            graph[i] = br.readLine();
        }
        int o = 0;
        int v = 0;
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };
        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if (graph[x].charAt(y) != '#' && !visited[x][y]) {
                    Queue<int[]> que = new ArrayDeque<>();
                    int no = 0;
                    int nv = 0;

                    visited[x][y] = true;
                    if (graph[x].charAt(y) == 'o') {
                        no++;
                    } else if (graph[x].charAt(y) == 'v') {
                        nv++;
                    }
                    que.add(new int[] { x, y });

                    while (que.size() != 0) {
                        int[] nq = que.poll();
                        for (int i = 0; i < 4; i++) {
                            if (0 <= nq[0] + dx[i] &&
                                    nq[0] + dx[i] < R &&
                                    0 <= nq[1] + dy[i] &&
                                    nq[1] + dy[i] < C &&
                                    graph[nq[0] + dx[i]].charAt(nq[1] + dy[i]) != '#' &&
                                    !visited[nq[0] + dx[i]][nq[1] + dy[i]]) {
                                visited[nq[0] + dx[i]][nq[1] + dy[i]] = true;
                                if (graph[nq[0] + dx[i]].charAt(nq[1] + dy[i]) == 'o') {
                                    no++;
                                } else if (graph[nq[0] + dx[i]].charAt(nq[1] + dy[i]) == 'v') {
                                    nv++;
                                }
                                que.add(new int[] { nq[0] + dx[i], nq[1] + dy[i] });
                            }
                        }
                    }
                    if (no > nv) {
                        o += no;
                    } else {
                        v += nv;
                    }
                }
            }
        }
        System.out.printf("%d %d", o, v);
    }
}