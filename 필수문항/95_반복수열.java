import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        List<Integer> D = new ArrayList<>();
        D.add(A);
        while (true) {
            String s = Integer.toString(D.get(D.size() - 1));
            int nextNum = 0;
            for (int i = 0; i < s.length(); i++) {
                nextNum += Math.pow(Integer.parseInt(Character.toString(s.charAt(i))), P);
            }
            for (int i = 0; i < D.size(); i++) {
                if (D.get(i) == nextNum) {
                    System.out.println(i);
                    return;
                }
            }
            D.add(nextNum);
        }
    }
}