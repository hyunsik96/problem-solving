import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String N = st.nextToken();
        int M = Integer.parseInt(st.nextToken());
        int lenN = N.length();

        if (lenN * Integer.parseInt(N) <= M) {
            for (int i = 0; i < Integer.parseInt(N); i++) {
                System.out.print(N);
            }
        } else {
            for (int i = 0; i < M / lenN; i++) {
                System.out.print(N);
            }
            for (int i = 0; i < M % lenN; i++) {
                System.out.print(N.charAt(i));
            }
        }
    }
}
