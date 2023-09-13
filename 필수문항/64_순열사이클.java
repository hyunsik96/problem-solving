import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sbAns = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {

            // test case
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] nums = new int[n + 1];
            boolean[] check = new boolean[n + 1];
            for (int m = 1; m <= n; m++) {
                nums[m] = Integer.parseInt(st.nextToken());
            }

            int ans = 0;

            for (int num = 1; num <= n; num++) {
                if (check[num]) {
                    continue;
                }

                ArrayList<Integer> tmp = new ArrayList<>();
                check[num] = true;
                tmp.add(num);
                int nextNum = nums[num];
                while (!check[nextNum] && !tmp.contains(nextNum)) {
                    check[nextNum] = true;
                    tmp.add(nextNum);
                    nextNum = nums[nextNum];
                }

                if (tmp.contains(nextNum)) {
                    ans++;
                }
            }
            sbAns.append(ans).append("\n");
            //

        }
        System.out.println(sbAns);
    }
}