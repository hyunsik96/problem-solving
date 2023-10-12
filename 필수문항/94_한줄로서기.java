import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            left[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> nList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nList.add(i);
        }

        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            ans[nList.get(left[i])] = i + 1;
            nList.remove(left[i]);
        }

        StringBuilder answer = new StringBuilder();
        for (int k : ans) {
            answer.append(k).append(' ');
        }
        System.out.println(answer);
    }
}