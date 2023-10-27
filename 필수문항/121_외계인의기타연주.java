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
        int ans = 0;
        int N = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        Stack<Integer>[] line = new Stack[7];
        for (int i = 1; i < 7; i++) {
            line[i] = new Stack<>();
        }
        while (N-- > 0) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            while (line[l].size() != 0 && line[l].get(line[l].size() - 1) > p) {
                line[l].pop();
                ans++;
            }
            if (line[l].size() == 0 || line[l].get(line[l].size() - 1) != p) {
                line[l].push(p);
                ans++;
            }
        }
        System.out.println(ans);
    }
}
