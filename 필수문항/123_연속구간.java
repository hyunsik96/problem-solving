import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String num = br.readLine();
            if (num == null) {
                return;
            }

            Character before = num.charAt(0);
            int ans = 1;
            int now = 1;
            for (int i = 1; i < num.length(); i++) {
                if (before == num.charAt(i)) {
                    now++;
                    ans = Math.max(ans, now);
                } else {
                    ans = Math.max(ans, now);
                    before = num.charAt(i);
                    now = 1;
                }
            }
            System.out.println(ans);
        }

    }
}
