import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] graph = new char[R][C];

        for (int i = 0; i < R; i++) {
            String s = br.readLine();
            for (int j = 0; j < C; j++) {
                graph[i][j] = s.charAt(j);
            }
        }

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if (graph[x][y] == 'S') {
                    for (int i = 0; i < 4; i++) {
                        if (0 <= x + dx[i] && x + dx[i] < R &&
                                0 <= y + dy[i] && y + dy[i] < C) {
                            if (graph[x + dx[i]][y + dy[i]] == 'W') {
                                System.out.println(0);
                                return;
                            }
                            if (graph[x + dx[i]][y + dy[i]] == '.') {
                                graph[x + dx[i]][y + dy[i]] = 'D';
                            }
                        }
                    }
                }
            }
        }
        System.out.println(1);
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                ans.append(graph[i][j]);
            }
            ans.append('\n');
        }
        ans.deleteCharAt(ans.length() - 1);
        System.out.println(ans);
    }
}

