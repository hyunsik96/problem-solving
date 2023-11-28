import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        testCase: while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            int[] graph = new int[n];
            for (int i = 0; i < n; i++) {
                graph[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(graph);
            int start = 0;
            int end = n;
            if (graph[0] == 0) {
                start = 1;
                if (n == 1) {
                    System.out.println("0 0");
                    continue testCase;
                }
            }
            if (graph[graph.length - 1] == l) {
                end -= 1;
                if (n - start - 1 == 0) {
                    System.out.println("0 0");
                    continue testCase;
                }
            }
            int minAns = Math.min(graph[start], l - graph[start]);
            int maxAns = graph[start];
            for (int i = start + 1; i < end; i++) {
                minAns = Math.max(minAns, Math.min(graph[i], l - graph[i]));
                maxAns += graph[i] - graph[i - 1];
            }
            maxAns += l - graph[end - 1];
            maxAns -= Math.min(graph[start], l - graph[end - 1]);
            System.out.printf("%d %d\n", minAns, maxAns);
        }
    }
}
