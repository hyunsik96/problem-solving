import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static int[][] foods;
    public static boolean[] visited;
    public static double ans = Double.POSITIVE_INFINITY;

    public static void comb(int num, int i) {
        if (i >= N) {
            return;
        }
        visited[i] = true;

        if (num == 1) {
            int s = 1;
            int b = 0;
            for (int k = 0; k < N; k++) {
                if (visited[k]) {
                    s *= foods[k][0];
                    b += foods[k][1];
                }
            }
            if (Math.abs(s - b) < ans) {
                ans = Math.abs(s - b);
            }
        } else {
            comb(num - 1, i + 1);
        }

        visited[i] = false;

        for (int j = i + 1; j < N; j++) {
            if (!visited[j]) {
                comb(num, j);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        foods = new int[N][2];
        visited = new boolean[N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            foods[i][0] = Integer.parseInt(st.nextToken());
            foods[i][1] = Integer.parseInt(st.nextToken());
        }

        // 1 개부터 N 개 까지 Combination으로 foods에서 뽑아 브루트포스
        for (int num = 1; num < N + 1; num++) {
            comb(num, 0);
        }
        System.out.println((int) ans);
    }
}