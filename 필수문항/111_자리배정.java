import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        if (K > C * R) {
            System.out.println(0);
        } else {
            int[][] graph = new int[C * R + 1][2];
            graph[0][0] = 1;
            int[] wall = { R, C, 1, 1 };
            int pointer = 0;

            for (int num = 1; num <= R * C; num++) {
                switch (pointer) {
                    case 0:
                        graph[num][0] = graph[num - 1][0];
                        graph[num][1] = graph[num - 1][1] + 1;
                        if (graph[num][1] == wall[pointer]) {
                            pointer = 1;
                            wall[3] += 1;
                        }
                        break;
                    case 1:
                        graph[num][1] = graph[num - 1][1];
                        graph[num][0] = graph[num - 1][0] + 1;
                        if (graph[num][0] == wall[pointer]) {
                            pointer = 2;
                            wall[0] -= 1;
                        }
                        break;
                    case 2:
                        graph[num][0] = graph[num - 1][0];
                        graph[num][1] = graph[num - 1][1] - 1;
                        if (graph[num][1] == wall[pointer]) {
                            pointer = 3;
                            wall[1] -= 1;
                        }
                        break;
                    case 3:
                        graph[num][1] = graph[num - 1][1];
                        graph[num][0] = graph[num - 1][0] - 1;
                        if (graph[num][0] == wall[pointer]) {
                            pointer = 0;
                            wall[2] += 1;
                        }
                        break;
                }
            }
            System.out.printf("%d %d", graph[K][0], graph[K][1]);
        }

    }
}