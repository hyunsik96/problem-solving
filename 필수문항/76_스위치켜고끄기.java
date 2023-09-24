import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] switches = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            switches[i] = Integer.parseInt(st.nextToken());
        }
        int num = Integer.parseInt(br.readLine());
        int gender = 0, number = 0;
        while (num-- > 0) {
            st = new StringTokenizer(br.readLine());
            gender = Integer.parseInt(st.nextToken());
            number = Integer.parseInt(st.nextToken());
            if (gender == 1) {
                int tmpNum = number;
                while (tmpNum <= n) {
                    switches[tmpNum] = switches[tmpNum] == 0 ? 1 : 0;
                    tmpNum += number;
                }
            } else {
                int lp = number, rp = number;
                while (true) {
                    if (0 < lp && rp <= n && switches[lp] == switches[rp]) {
                        lp -= 1;
                        rp += 1;
                    } else {
                        lp += 1;
                        rp -= 1;
                        break;
                    }
                }
                for (int i = lp; i <= rp; i++) {
                    switches[i] = switches[i] == 0 ? 1 : 0;
                }
            }
        }

        int start = 1;
        int end = 20;

        while (true) {
            if (end > n) {
                end = n;
            }
            if (start > n) {
                break;
            }
            for (int i = start; i <= end; i++) {
                ans.append(switches[i]).append(" ");
            }
            ans.append("\n");
            start += 20;
            end += 20;
        }
        System.out.println(ans);
    }
}
