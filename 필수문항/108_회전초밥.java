import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        Map<Integer, Integer> dic = new HashMap<>();

        dic.put(c, 1);
        for (int i = 0; i < k; i++) {
            if (dic.containsKey(sushi[i])) {
                dic.put(sushi[i], dic.get(sushi[i]) + 1);
            } else {
                dic.put(sushi[i], 1);
            }
        }
        int ans = dic.size();

        for (int i = 1; i < N; i++) {
            if (dic.get(sushi[i - 1]) == 1) {
                dic.remove(sushi[i - 1]);
            } else {
                dic.put(sushi[i - 1], dic.get(sushi[i - 1]) - 1);
            }

            if (dic.containsKey(sushi[(i + k - 1) % N])) {
                dic.put(sushi[(i + k - 1) % N], dic.get(sushi[(i + k - 1) % N]) + 1);
            } else {
                dic.put(sushi[(i + k - 1) % N], 1);
            }
            ans = Integer.max(ans, dic.size());
        }
        System.out.println(ans);
    }
}