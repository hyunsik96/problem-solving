import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int pentaX;
    static int pentaY;
    static int[][] conv;
    static boolean[] visited;

    public static boolean bfs(int startX, int startY) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(startX);
        queue.add(startY);

        while (!queue.isEmpty()) {
            int x = queue.poll();
            int y = queue.poll();

            if (1000 >= (Math.abs(x - pentaX) + Math.abs(y - pentaY))) {
                return true;
            }

            for (int i = 0; i < conv.length; i++) {
                if (!visited[i] && 1000 >= (Math.abs(x - conv[i][0]) + Math.abs(y - conv[i][1]))) {
                    visited[i] = true;
                    queue.add(conv[i][0]);
                    queue.add(conv[i][1]);
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int count = Integer.parseInt(br.readLine());
            StringTokenizer stH = new StringTokenizer(br.readLine());
            int houseX = Integer.parseInt(stH.nextToken());
            int houseY = Integer.parseInt(stH.nextToken());
            conv = new int[count][2];
            for (int i = 0; i < count; i++) {
                StringTokenizer stC = new StringTokenizer(br.readLine());
                conv[i][0] = Integer.parseInt(stC.nextToken());
                conv[i][1] = Integer.parseInt(stC.nextToken());
            }
            StringTokenizer stP = new StringTokenizer(br.readLine());

            pentaX = Integer.parseInt(stP.nextToken());
            pentaY = Integer.parseInt(stP.nextToken());
            visited = new boolean[count];

            if (bfs(houseX, houseY)) {
                ans.append("happy").append("\n");
            } else {
                ans.append("sad").append("\n");
            }
        }
        System.out.println(ans);
    }
}
