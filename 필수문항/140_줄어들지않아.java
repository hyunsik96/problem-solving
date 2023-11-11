import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            BigInteger ans = new BigInteger("1");
            for (int i = 0; i < N; i++) {
                ans = ans.multiply(BigInteger.valueOf(10 + N - 1 - i));
            }
            for (int i = N; i >= 1; i--) {
                ans = ans.divide(BigInteger.valueOf(i));
            }
            System.out.println(ans);
        }

    }
}
