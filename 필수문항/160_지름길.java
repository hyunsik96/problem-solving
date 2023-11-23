import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static List<Integer[]> routes = new ArrayList<>();
    private static int ans;
    private static int N;

    private static void dfs(int idx, int D) {
        D -= routes.get(idx)[2];
        boolean check = false;
        for (int i = idx + 1; i < N; i++) {
            if (routes.get(idx)[1] <= routes.get(i)[0]) {
                check = true;
                dfs(i, D);
            }
        }
        if (!check) {
            ans = Math.min(ans, D);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        ans = D;
        while (N-- > 0) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int price = Integer.parseInt(st.nextToken());
            if (to > D || to - from - price <= 0) {
                continue;
            }
            routes.add(new Integer[] { from, to, to - from - price });
        }
        N = routes.size();
        routes.sort(new Comparator<Integer[]>() {
            @Override
            public int compare(Integer[] o1, Integer[] o2) {
                if (o1[0] < o2[0]) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });

        for (int i = 0; i < N; i++) {
            dfs(i, D);
        }
        System.out.println(ans);
    }
}
