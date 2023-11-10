import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] moneys = new int[N];
        int max = 0;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            moneys[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, moneys[i]);
            sum += moneys[i];
        }
        int lp = max;
        int rp = sum;
        while (lp <= rp) {
            int mid = (lp + rp) / 2;
            int tmpAns = 1;
            int tmpSum = 0;
            for (int money : moneys) {
                if (money + tmpSum > mid) {
                    tmpAns++;
                    tmpSum = money;
                } else {
                    tmpSum += money;
                }
            }
            if (tmpAns > M) {
                lp = mid + 1;
            } else {
                rp = mid - 1;
            }
        }
        System.out.println(lp);
    }
}
