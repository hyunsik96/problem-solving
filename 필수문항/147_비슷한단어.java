import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String basic = br.readLine();
        int ans = 0;
        while (N-- > 1) {
            char[] word = br.readLine().toCharArray();
            int onlyBasic = 0;
            int onlyWord = 0;
            for (int i = 0; i < basic.length(); i++) {
                boolean check = false;
                for (int j = 0; j < word.length; j++) {
                    if (word[j] == basic.charAt(i)) {
                        word[j] = '*';
                        check = true;
                        break;
                    }
                }
                if (!check) {
                    onlyBasic++;
                }
            }
            for (char c : word) {
                if (c != '*') {
                    onlyWord++;
                }
            }
            if (Math.abs(basic.length() - word.length) <= 1 && onlyWord <= 1 && onlyBasic <= 1) {
                ans++;
            }

        }
        System.out.println(ans);
    }
}
