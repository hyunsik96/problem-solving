import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static int ans = 0;
    public static int N;
    public static int K;
    public static Queue<Integer> que;
    public static char[] table;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        table = br.readLine().toCharArray();
        que = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            switch (table[i]) {
                case 'H':
                    que.add(i);
                    break;
                case 'P':
                    findH(i);
            }
        }
        System.out.println(ans);
    }

    public static void findH(int i) {
        while (que.size() != 0) {
            int h = que.poll();
            if (i - h <= K) {
                ans++;
                return;
            }
        }
        for (int l = i + 1; l < Math.min(i + K + 1, N); l++) {
            if (table[l] == 'H') {
                ans++;
                table[l] = 'X';
                return;
            }
        }
    }

}
