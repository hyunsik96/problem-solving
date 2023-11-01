import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int D = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] a = new int[D];
        int[] b = new int[D];
        a[0] = 1;
        b[1] = 1;
        for (int i = 2; i < D; i++) {
            a[i] = a[i - 2] + a[i - 1];
            b[i] = b[i - 2] + b[i - 1];
        }
        for (int i = 1; i < 100000; i++) {
            if ((K - a[D - 1] * i) % b[D - 1] == 0) {
                System.out.println(i);
                System.out.println((K - a[D - 1] * i) / b[D - 1]);
                break;
            }
        }
    }
}
