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
        int[][] candidates = new int[3][5];
        candidates[0][4] = 1;
        candidates[1][4] = 2;
        candidates[2][4] = 3;

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int l = 0; l < 3; l++) {
                int tmp = Integer.parseInt(st.nextToken());
                candidates[l][0] += tmp;
                candidates[l][4 - tmp] += 1;
            }
        }
        Arrays.sort(candidates, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] < o2[0]) {
                    return 1;
                } else if ((o1[0] > o2[0])) {
                    return -1;
                } else if (o1[1] < o2[1]) {
                    return 1;
                } else if ((o1[1] > o2[1])) {
                    return -1;
                } else if (o1[2] < o2[2]) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });
        if (candidates[0][0] == candidates[1][0] && candidates[0][1] == candidates[1][1]
                && candidates[0][2] == candidates[1][2]) {
            System.out.printf("0 %d", candidates[0][0]);
        } else {
            System.out.printf("%d %d", candidates[0][4], candidates[0][0]);
        }

    }
}
