import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Float> dic = new HashMap<>();
        float total = 0f;
        while (true) {
            String name = br.readLine();
            if (name == null || name.length() == 0) {
                break;
            }
            total++;
            if (dic.get(name) != null) {
                dic.put(name, dic.get(name) + 1f);
            } else {
                dic.put(name, 1f);
            }
        }

        Map<String, Float> sortedMap = new TreeMap<>(dic);
        for (String entry : sortedMap.keySet()) {
            System.out.printf("%s %.4f\n", entry, sortedMap.get(entry) * 100 / total);
        }

    }
}
