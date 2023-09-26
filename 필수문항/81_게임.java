import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long total = Integer.parseInt(st.nextToken()); // 총 게임 횟수
        long win = Integer.parseInt(st.nextToken()); // 이긴 횟수
        long now = win * 100 / total;
        if (now >= 99) {
            System.out.println(-1);
        } else {
            long top = ((now + 1) * total - 100 * win);
            long bot = (99 - now);
            System.out.println(((int) Math.ceil((double) top / (double) bot)));
        }
    }
}
