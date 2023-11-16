import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        StringTokenizer st;
        String S = br.readLine();
        int[][] alphabet = new int[26][S.length()];
        alphabet[(int) S.charAt(0) - 97][0] = 1;
        for (int i = 1; i < S.length(); i++) {
            alphabet[(int) S.charAt(i) - 97][i] = 1;
            for (int[] alpha : alphabet) {
                alpha[i] += alpha[i - 1];
            }
        }

        int q = Integer.parseInt(br.readLine());
        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());
            int c = (int) st.nextToken().charAt(0) - 97;
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            if (start == 0) {
                ans.append(alphabet[c][end]).append('\n');
            } else {
                ans.append(alphabet[c][end] - alphabet[c][start - 1]).append('\n');
            }
        }
        System.out.println(ans);
    }
}
