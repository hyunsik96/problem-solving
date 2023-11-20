import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int[] ans;
    private static int[][] cards;

    private static void comb(int cardIdx, int[] now, int idx, int from) {
        if (idx == 3) {
            if (Arrays.stream(now).sum() % 10 > ans[cardIdx]) {
                ans[cardIdx] = Arrays.stream(now).sum() % 10;
            }
            return;
        }
        for (int i = from; i < 5; i++) {
            now[idx] = cards[cardIdx][i];
            comb(cardIdx, now, idx + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        cards = new int[n][5];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                cards[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = new int[n];
        for (int i = 0; i < n; i++) {
            comb(i, new int[] { 0, 0, 0 }, 0, 0);
        }
        int ansNum = -1;
        int ansIdx = -1;
        for (int i = 0; i < n; i++) {
            if (ans[i] >= ansNum) {
                ansIdx = i;
                ansNum = ans[i];
            }
        }
        System.out.println(ansIdx + 1);
    }
}
