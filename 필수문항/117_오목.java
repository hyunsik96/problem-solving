import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static int[][] graph = new int[19][19];
    public static int[][] direction = { { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, -1 } };

    public static boolean valid(int x, int y, int num) {
        return 0 <= x && x < 19 && 0 <= y && y < 19 && graph[x][y] == num;
    }

    public static int check(int x, int y, int dx, int dy) {
        int count = 1;
        int num = graph[x][y];
        while (valid(x + dx, y + dy, num)) {
            x += dx;
            y += dy;
            count++;
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 19; i++) {
            graph[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int x = 0; x < 19; x++) {
            for (int y = 0; y < 19; y++) {
                if (graph[x][y] != 0) {
                    for (int[] d : direction) {
                        int dx = d[0];
                        int dy = d[1];
                        int count = 1;

                        if (valid(x + dx, y + dy, graph[x][y])) {
                            count += check(x + dx, y + dy, dx, dy);
                        }

                        if (valid(x - dx, y - dy, graph[x][y])) {
                            count += check(x - dx, y - dy, -dx, -dy);
                        }

                        if (count == 5) {
                            if (dy == 1) {
                                dx = -dx;
                                dy = -dy;
                            } else if (dy == 0 && dx == 1) {
                                dx = -dx;
                            }
                            int num = graph[x][y];
                            while (valid(x + dx, y + dy, num)) {
                                y += dy;
                                x += dx;
                            }
                            System.out.println(num);
                            System.out.printf("%d %d", x + 1, y + 1);
                            return;
                        }
                    }
                }
            }
        }
        System.out.println(0);

    }
}
