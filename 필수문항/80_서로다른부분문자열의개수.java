import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();

        String word = br.readLine();
        int wordLen = word.length();
        Set<String> stringSet = new HashSet<>();

        for (int len = 1; len <= wordLen; len++) {
            for (int i = 0; i <= wordLen - len; i++) {
                stringSet.add(word.substring(i, i + len));
            }
        }
        System.out.println(stringSet.size());
    }
}

