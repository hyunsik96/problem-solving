import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int score = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        if (N == 0) {
            System.out.println(1);
            return;
        }
        Integer[] scores = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        Arrays.sort(scores, (a, b) -> b - a);

        int lp = 0;
        int rp = N - 1;
        while (lp <= rp) {
            int mid = (lp + rp) / 2;

            if (scores[mid] > score) {
                lp = mid + 1;
            } else {
                rp = mid - 1;
            }
        }
        int ans = lp;
        while (lp < N && scores[lp] == score) {
            lp++;
        }
        if (lp + 1 > P) {
            System.out.println(-1);
        } else {
            System.out.println(ans + 1);
        }

    }
}
