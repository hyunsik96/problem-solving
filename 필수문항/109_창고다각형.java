import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] graph = new int[1001];
        int tall = 0;
        StringTokenizer st;
        while (N-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a] = b;
            tall = Integer.max(tall, b);
        }
        int lp = 1;
        int rp = 1000;

        int ls = 1;
        int rs = 1000;

        int ans = 0;

        while (graph[lp] != tall) {
            if (graph[lp] > graph[ls]) {
                ans += (lp - ls) * graph[ls];
                ls = lp;
            }
            lp++;
        }
        ans += (lp - ls) * graph[ls];

        while (graph[rp] != tall) {
            if (graph[rp] > graph[rs]) {
                ans += (rs - rp) * graph[rs];
                rs = rp;
            }
            rp--;
        }
        ans += (rs - rp) * graph[rs];
        ans += (rp - lp + 1) * tall;
        System.out.println(ans);
    }
}