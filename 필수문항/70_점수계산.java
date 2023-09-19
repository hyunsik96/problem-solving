import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int total = 0;
        int[] scores = new int[8];
        boolean[] check = new boolean[8];
        for (int i = 0; i < 8; i++) {
            scores[i] = Integer.parseInt(br.readLine());
        }
        int[] scoresDup = Arrays.copyOf(scores, 8);
        Arrays.sort(scores);
        for (int i = 0; i < 8; i++) {
            if (scoresDup[i] == scores[0] || scoresDup[i] == scores[1] || scoresDup[i] == scores[2]) {
                check[i] = true;
            } else {
                total += scoresDup[i];
            }
        }
        ans.append(total).append("\n");
        for (int i = 0; i < 8; i++) {
            if (!check[i]) {
                ans.append(i + 1).append(" ");
            }
        }
        System.out.println(ans);
    }
}
