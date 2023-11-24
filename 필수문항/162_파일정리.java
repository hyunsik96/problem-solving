import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Map<String, Integer> dic = new HashMap<>();
        while (n-- > 0) {
            String word = br.readLine().split("\\.")[1];
            if (dic.containsKey(word)) {
                dic.put(word, dic.get(word) + 1);
            } else {
                dic.put(word, 1);
            }
        }
        Object[] keys = dic.keySet().toArray();
        Arrays.sort(keys);
        StringBuilder ans = new StringBuilder();
        for (Object key : keys) {
            ans.append(key).append(" ").append(dic.get(key)).append("\n");
        }
        ans.deleteCharAt(ans.length() - 1);
        System.out.println(ans);
    }
}
