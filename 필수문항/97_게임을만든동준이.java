import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] level = new int[N];
        for (int i = 0; i < N; i++) {
            level[i] = Integer.parseInt(br.readLine());
        }
        int ans = 0;
        for (int i = N - 2; i > -1; i--) {
            if (level[i + 1] <= level[i]) {
                ans += level[i] - level[i + 1] + 1;
                level[i] = level[i + 1] - 1;
            }
        }
        System.out.println(ans);
    }

}