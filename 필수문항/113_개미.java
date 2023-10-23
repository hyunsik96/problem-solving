import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(br.readLine());

        p += t;
        q += t;
        if (p / w % 2 == 0) {
            p %= w;
        } else {
            p = w - p % w;
        }
        if (q / h % 2 == 0) {
            q %= h;
        } else {
            q = h - q % h;
        }
        System.out.printf("%d %d", p, q);
    }
}