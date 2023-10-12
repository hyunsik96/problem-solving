import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();
        Map<Character, Integer> dic = new HashMap<>();
        List<Character> cList = new ArrayList<>();
        for (int i = 0; i < name.length(); i++) {
            if (dic.containsKey(name.charAt(i))) {
                dic.put(name.charAt(i), dic.get(name.charAt(i)) + 1);
            } else {
                dic.put(name.charAt(i), 1);
                cList.add(name.charAt(i));
            }
        }
        Collections.sort(cList);
        String halfAns = "";
        Character center = ' ';

        for (Character c : cList) {
            if (dic.get(c) % 2 == 1) {
                if (center != ' ') {
                    System.out.println("I'm Sorry Hansoo");
                    return;
                } else {
                    center = c;
                    dic.put(c, dic.get(c) - 1);
                    for (int i = 0; i < dic.get(c) / 2; i++) {
                        halfAns += c;
                    }
                }
            } else {
                for (int i = 0; i < dic.get(c) / 2; i++) {
                    halfAns += c;
                }
            }
        }
        String ans = "" + halfAns;
        if (center != ' ') {
            ans += center;
        }
        for (int i = halfAns.length() - 1; i >= 0; i--) {
            ans += halfAns.charAt(i);
        }
        System.out.println(ans);
    }
}