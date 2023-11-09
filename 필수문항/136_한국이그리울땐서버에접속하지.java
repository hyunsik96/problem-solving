import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String word = br.readLine();
        StringTokenizer st = new StringTokenizer(word, "*");
        String prefix = st.nextToken();
        String suffix = st.nextToken();

        test: while (N-- > 0) {
            String pattern = br.readLine();
            if (pattern.length() < word.length() - 1) {
                System.out.println("NE");
            } else {
                for (int i = 0; i < prefix.length(); i++) {
                    if (prefix.charAt(i) != pattern.charAt(i)) {
                        System.out.println("NE");
                        continue test;
                    }
                }
                for (int i = pattern.length() - suffix.length(); i < pattern.length(); i++) {
                    if (suffix.charAt(i - pattern.length() + suffix.length()) != pattern.charAt(i)) {
                        System.out.println("NE");
                        continue test;
                    }
                }
                System.out.println("DA");
            }
        }
    }
}
