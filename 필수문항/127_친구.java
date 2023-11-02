import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer>[] friends = new List[N];
        boolean[][] graph = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            friends[i] = new ArrayList<>();
            String word = br.readLine();
            for (int idx = 0; idx < N; idx++) {
                if (word.charAt(idx) == 'Y') {
                    graph[i][idx] = true;
                    friends[i].add(idx);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int f : friends[i]) {
                for (int ff : friends[f]) {
                    graph[i][ff] = true;
                }
            }
        }
        int ans = 0;
        for (boolean[] g : graph) {
            int tmp_ans = 0;
            for (boolean gg : g) {
                if (gg) {
                    tmp_ans++;
                }
            }
            ans = ans < tmp_ans ? tmp_ans : ans;
        }
        System.out.println(ans == 0 ? ans : ans - 1);
    }
}
