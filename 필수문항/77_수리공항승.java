import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), l = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] hole = new int[n];
        for (int i = 0; i < n; i++) {
            hole[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(hole);
        int ans = 0;
        double rp = -1;
        for (int i = 0; i < n; i++) {
            if (hole[i] + 0.5 <= rp) {
                continue;
            } else {
                ans++;
                rp = hole[i] - 0.5 + l;
            }
        }
        System.out.println(ans);
    }
}
