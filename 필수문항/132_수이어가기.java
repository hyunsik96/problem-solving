import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        int k = 2;
        int lt = 1;
        int lb = 1;
        int rt = 1;
        int rb = 1;
        int lp = 1;
        int rp = num;
        int x = 1;

        while (lp <= rp) {
            k++;
            x = lp;
            if (k % 2 == 1) {
                lt = rb;
                lb = rt + rb;
                if (lt * num % lb == 0) {
                    lp = lt * num / lb;
                } else {
                    lp = lt * num / lb + 1;
                }
            } else {
                rt = lb;
                rb = lt + lb;
                rp = rt * num / rb;
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(k).append("\n").append(num).append(" ").append(x);
        while (num - x >= 0) {
            sb.append(" ").append(num - x);
            x = num - x;
            num = num - x;
        }
        System.out.println(sb);
    }
}
