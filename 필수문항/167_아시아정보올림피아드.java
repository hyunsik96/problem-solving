import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] scores = new int[n][3];
        int[] nations = new int[101];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            scores[i][0] = Integer.parseInt(st.nextToken());
            scores[i][1] = Integer.parseInt(st.nextToken());
            scores[i][2] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(scores, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[2] < o2[2]) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });
        int ans = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (nations[scores[i][0]] < 2) {
                sb.append(scores[i][0]).append(' ').append(scores[i][1]).append('\n');
                if (ans == 2) {
                    break;
                }
                ans++;
                nations[scores[i][0]]++;
            }
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb);
    }
}

