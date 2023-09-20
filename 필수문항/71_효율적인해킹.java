import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            graph[Integer.parseInt(st.nextToken())].add(Integer.parseInt(st.nextToken()));
        }

        int[] num = new int[N + 1];
        int maxNum = 0;

        for (int i = 1; i < N + 1; i++) {
            boolean[] check = new boolean[N + 1];
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(i);
            check[i] = true;
            while (!queue.isEmpty()) {
                int point = queue.remove();
                for (int p : graph[point]) {
                    if (!check[p]) {
                        queue.add(p);
                        check[p] = true;
                        num[p] += 1;
                    }
                }
            }
        }

        for (int i = 1; i < N + 1; i++) {
            if (num[i] > maxNum) {
                maxNum = num[i];
            }
        }
        for (int i = 1; i < N + 1; i++) {
            if (num[i] == maxNum) {
                ans.append(i).append(" ");
            }
        }
        System.out.println(ans);
    }
}


