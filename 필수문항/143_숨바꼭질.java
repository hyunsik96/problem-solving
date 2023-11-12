import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        while (M-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
        Queue<Integer[]> que = new ArrayDeque<>();
        int[] distance = new int[N + 1];
        Arrays.fill(distance, -1);
        distance[1] = 0;
        for (int i : graph[1]) {
            que.add(new Integer[] { i, 1 });
            distance[i] = 1;
        }
        while (que.size() != 0) {
            Integer[] tmp = que.poll();
            for (int place : graph[tmp[0]]) {
                if (distance[place] == -1) {
                    distance[place] = tmp[1] + 1;
                    que.add(new Integer[] { place, distance[place] });
                }
            }
        }
        int place = 1;
        int max = 0;
        int num = 1;
        for (int p = 2; p <= N; p++) {
            if (distance[p] > max) {
                max = distance[p];
                place = p;
                num = 1;
            } else if (distance[p] == max) {
                num++;
            }
        }
        System.out.printf("%d %d %d", place, max, num);
    }
}
