import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String doc;
    static String word;
    static int docLen;
    static int wordLen;

    private static boolean check(int pointer) {
        for (int i = 0; i < wordLen; i++) {
            if (doc.charAt(pointer + i) != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;
        doc = br.readLine();
        word = br.readLine();
        docLen = doc.length();
        wordLen = word.length();
        int pointer = 0;
        while (pointer + wordLen <= docLen) {
            if (check(pointer)) {
                ans++;
                pointer += wordLen;
            } else {
                pointer++;
            }
        }
        System.out.println(ans);
    }
}