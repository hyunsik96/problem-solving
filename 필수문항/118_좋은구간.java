import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        int[] good = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        int n = Integer.parseInt(br.readLine());

        int pl = 0;
        int pr = L - 1;
        while (pl < pr) {
            int mid = (pl + pr) / 2;
            if (good[mid] > n) {
                pr = mid - 1;
            } else if (good[mid] < n) {
                pl = mid + 1;
            } else {
                pl = mid;
                pr = mid;
            }
        }
        if (good[pl] > n) {
            int l = pl == 0 ? 0 : good[pl - 1];
            int r = good[pl];
            System.out.println((n - l) * (r - n) - 1);
        } else if (good[pl] < n) {
            int l = good[pl];
            int r = good[pl + 1];
            System.out.println((n - l) * (r - n) - 1);
        } else {
            System.out.println(0);
        }

    }
}
