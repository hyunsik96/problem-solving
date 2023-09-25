import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[][] check = new boolean[100][100];
        StringTokenizer st;
        int xl = 0, yl = 0, xr = 0, yr = 0;
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            xl = Integer.parseInt(st.nextToken());
            yl = Integer.parseInt(st.nextToken());
            xr = Integer.parseInt(st.nextToken());
            yr = Integer.parseInt(st.nextToken());
            for (int x = xl; x < xr; x++) {
                for (int y = yl; y < yr; y++) {
                    check[x][y] = true;
                }
            }
        }
        int ans = 0;
        for (int x = 1; x < 100; x++) {
            for (int y = 1; y < 100; y++) {
                if (check[x][y]) {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
