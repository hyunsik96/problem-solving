import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int total = 0;
        int ans = 2100000000;

        int[][] graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            StringTokenizer tmpSt = new StringTokenizer(br.readLine());
            for (int l = 0; l < m; l++) {
                graph[i][l] = Integer.parseInt(tmpSt.nextToken());
                total += graph[i][l];
            }
        }

        int height = total / (n * m);

        int tmpAns = 0;

        while (true) {
            for (int i = 0; i < n; i++) {
                for (int l = 0; l < m; l++) {
                    if (graph[i][l] < height) {
                        tmpAns += height - graph[i][l];
                    } else {
                        tmpAns += (graph[i][l] - height) * 2;
                    }
                }
            }
            if (tmpAns <= ans) {
                ans = tmpAns;
                if ((height + 1) * (m * n) - total <= b) {
                    height++;
                    tmpAns = 0;
                } else {
                    break;
                }
            } else {
                height--;
                break;
            }
        }

        System.out.println(sb.append(ans).append(" ").append(height));
    }
}