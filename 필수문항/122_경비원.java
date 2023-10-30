import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());
        int[] len = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            switch (d) {
                case 1:
                    len[i] = -y - l;
                    break;
                case 2:
                    len[i] = l;
                    break;
                case 3:
                    len[i] = -y + l;
                    break;
                case 4:
                    len[i] = x + y - l;
                    break;
            }
        }
        int ans = 0;
        int total = 2 * (x + y);
        for (int i = 0; i < n; i++) {
            int l = Math.abs(len[n] - len[i]);
            ans += Math.min(l, total - l);
        }
        System.out.println(ans);
    }
}
