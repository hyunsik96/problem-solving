import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] dolls = new int[n];
        for (int i = 0; i < n; i++) {
            dolls[i] = Integer.parseInt(st.nextToken());
        }

        double ans = solve(n, k, dolls);
        System.out.println(Math.sqrt(ans));
    }

    private static double getB(int[] dolls, int i, int k, double m) {
        double s = 0;
        for (int idx = i; idx < i + k; idx++) {
            s += Math.pow(dolls[idx] - m, 2);
        }
        return s / k;
    }

    private static double solve(int n, int k, int[] dolls) {
        double s = 0;
        for (int i = 0; i < k; i++) {
            s += dolls[i];
        }

        double ans = getB(dolls, 0, k, s / k);

        double tmpSum = s;

        for (int i = 1; i <= n - k; i++) {
            tmpSum += dolls[k + i - 1];
            ans = Math.min(ans, getB(dolls, 0, k + i, tmpSum / (k + i)));
        }

        for (int now = 1; now <= n - k; now++) {
            s -= dolls[now - 1] - dolls[now + k - 1];

            ans = Math.min(ans, getB(dolls, now, k, s / k));
            tmpSum = s;

            for (int i = 1; i <= n - k - now; i++) {
                tmpSum += dolls[now + k + i - 1];
                ans = Math.min(ans, getB(dolls, now, k + i, tmpSum / (k + i)));
            }
        }

        return ans;
    }
}
