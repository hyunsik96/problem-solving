import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] homes = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        for (int i = 1; i < N; i++) {
            int diff = (homes[i] - homes[i - 1]) * (2 * i - N);
            if (diff > 0 || (diff == 0 && homes[i] != homes[i - 1])) {
                System.out.println(homes[i - 1]);
                return;
            }
        }
        System.out.println(homes[N - 1]);
    }
}
