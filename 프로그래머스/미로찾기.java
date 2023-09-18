import java.util.ArrayDeque;
import java.util.Queue;

class Solution {

    public int solution(String[] maps) {
        int xLen = maps.length;
        int yLen = maps[0].length();
        int sX = 0, sY = 0, lX = 0, lY = 0, eX = 0, eY = 0;
        boolean foundS = false, foundL = false, foundE = false;
        for (int x = 0; x < xLen; x++) {
            for (int y = 0; y < yLen; y++) {
                if (!foundS && maps[x].charAt(y) == ('S')) {
                    foundS = true;
                    sX = x;
                    sY = y;
                } else if (!foundL && maps[x].charAt(y) == ('L')) {
                    foundL = true;
                    lX = x;
                    lY = y;
                } else if (!foundE && maps[x].charAt(y) == ('E')) {
                    foundE = true;
                    eX = x;
                    eY = y;
                }
            }
        }

        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] { sX, sY, 0 });
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };
        boolean[][] visited = new boolean[xLen][yLen];
        int ansL = -1;
        while (!queue.isEmpty()) {
            int[] tmp = queue.remove();
            int x = tmp[0], y = tmp[1], count = tmp[2];
            if (x == lX && y == lY) {
                ansL = count;
                break;
            }
            for (int i = 0; i < 4; i++) {
                if (0 <= x + dx[i] && x + dx[i] < xLen && 0 <= y + dy[i] && y + dy[i] < yLen
                        && maps[x + dx[i]].charAt(y + dy[i]) != 'X' && !visited[x + dx[i]][y + dy[i]]) {
                    visited[x + dx[i]][y + dy[i]] = true;
                    queue.add(new int[] { x + dx[i], y + dy[i], count + 1 });
                }
            }
        }
        if (ansL == -1) {
            return -1;
        }

        queue = new ArrayDeque<>();
        queue.add(new int[] { lX, lY, 0 });
        visited = new boolean[xLen][yLen];
        int ansE = -1;
        while (!queue.isEmpty()) {
            int[] tmp = queue.remove();
            int x = tmp[0], y = tmp[1], count = tmp[2];
            if (x == eX && y == eY) {
                ansE = count;
                break;
            }
            for (int i = 0; i < 4; i++) {
                if (0 <= x + dx[i] && x + dx[i] < xLen && 0 <= y + dy[i] && y + dy[i] < yLen
                        && maps[x + dx[i]].charAt(y + dy[i]) != 'X' && !visited[x + dx[i]][y + dy[i]]) {
                    visited[x + dx[i]][y + dy[i]] = true;
                    queue.add(new int[] { x + dx[i], y + dy[i], count + 1 });
                }
            }
        }
        if (ansE == -1) {
            return -1;
        }

        return ansL + ansE;
    }
}

public class Main {
    public static void main(String[] args) {
        String[] maps = { "SLOOO", "XXXXO", "OOOOO", "OXXXX", "EOOOO" };
        Solution test = new Solution();
        System.out.println(test.solution(maps));
    }
}
