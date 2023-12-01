import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] inList = new String[n];
        String[] outList = new String[n];
        for (int i = 0; i < n; i++) {
            inList[i] = br.readLine();
        }
        for (int i = 0; i < n; i++) {
            outList[i] = br.readLine();
        }
        int now = -1;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = now + 1; j < n; j++) {
                if (inList[i].equals(outList[j])) {
                    ans++;
                    now = j;
                    break;
                }
            }
        }
        System.out.println(n - ans);
    }
}
