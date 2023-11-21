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
        int[][] points = new int[n][2];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            points[i][1] = Integer.parseInt(st.nextToken());
            points[i][0] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(points, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] < o2[0]) {
                    return -1;
                } else if (o1[0] > o2[0]) {
                    return 1;
                } else if (o1[1] < o2[1]) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int ans = 100000;
            if (0 < i && points[i - 1][0] == points[i][0]) {
                ans = points[i][1] - points[i - 1][1];
            }
            if (i < n - 1 && points[i + 1][0] == points[i][0]) {
                ans = Math.min(ans, points[i + 1][1] - points[i][1]);
            }
            answer += ans;
        }
        System.out.println(answer);
    }
}

