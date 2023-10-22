import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Map<Character, Integer>[] check = new HashMap[M];
        for (int i = 0; i < M; i++) {
            check[i] = new HashMap<>();
            check[i].put('A', 0);
            check[i].put('C', 0);
            check[i].put('G', 0);
            check[i].put('T', 0);
        }

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            for (int l = 0; l < M; l++) {
                check[l].put(word.charAt(l), check[l].get(word.charAt(l)) + 1);
            }
        }

        StringBuilder ans = new StringBuilder();
        int ansNum = 0;

        Character[] test = { 'A', 'C', 'G', 'T' };
        for (int i = 0; i < M; i++) {
            Character tmpC = 'A';
            int tmpN = 0;
            for (Character c : test) {
                if (check[i].get(c) > tmpN) {
                    tmpC = c;
                    tmpN = check[i].get(c);
                }
            }
            ans.append(tmpC);
            ansNum += N - tmpN;
        }
        System.out.println(ans);
        System.out.println(ansNum);
    }
}