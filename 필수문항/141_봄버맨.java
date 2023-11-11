//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.*;
//
//public class Main {
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        int R = Integer.parseInt(st.nextToken());
//        int C = Integer.parseInt(st.nextToken());
//        int N = Integer.parseInt(st.nextToken());
//        int[] dx = {1, -1, 0, 0};
//        int[] dy = {0, 0, 1, -1};
//        char[][] graph = new char[R][C];
//        for (int i = 0; i < R; i++) {
//            graph[i] = br.readLine().toCharArray();
//        }
//
//        if (N == 1) {
//            for (int x = 0; x < R; x++) {
//                for (int y = 0; y < C; y++) {
//                    System.out.print(graph[x][y]);
//                }
//                System.out.println();
//            }
//        } else if (N % 2 == 0) {
//            for (int x = 0; x < R; x++) {
//                for (int y = 0; y < C; y++) {
//                    System.out.print("O");
//                }
//                System.out.println();
//            }
//        } else {
//            N /= 2;
//
//            Set<Map.Entry<Integer, Integer>> bomb = new HashSet<>();
//            for (int x = 0; x < R; x++) {
//                for (int y = 0; y < C; y++) {
//                    if (graph[x][y] == 'O') {
//                        bomb.add(new AbstractMap.SimpleEntry<>(x, y));
//                    }
//                }
//            }
//
//            while (N-- > 0) {
//                Set<Map.Entry<Integer, Integer>> blank = new HashSet<>();
//                for (Map.Entry<Integer, Integer> xy : bomb) {
//                    int x = xy.getKey();
//                    int y = xy.getValue();
//                    blank.add(new AbstractMap.SimpleEntry<>(x, y));
//                    for (int i = 0; i < 4; i++) {
//                        if (0 <= x + dx[i] &&
//                                x + dx[i] < R &&
//                                0 <= y + dy[i] &&
//                                y + dy[i] < C
//                        ) {
//                            blank.add(new AbstractMap.SimpleEntry<>(x + dx[i], y + dy[i]));
//                        }
//                    }
//                }
//                bomb = new HashSet<>();
//                for (int nx = 0; nx < R; nx++) {
//                    for (int ny = 0; ny < C; ny++) {
//                        boolean check = true;
//                        for (Map.Entry<Integer, Integer> bxy : blank) {
//                            int bx = bxy.getKey();
//                            int by = bxy.getValue();
//                            if (nx == bx && ny == by) {
//                                check = false;
//                                break;
//                            }
//                        }
//                        if (check) {
//                            bomb.add(new AbstractMap.SimpleEntry<>(nx, ny));
//                        }
//                    }
//                }
//            }
//
//            for (int i = 0; i < R; i++) {
//                Arrays.fill(graph[i], '.');
//            }
//            for (Map.Entry<Integer, Integer> bxy : bomb) {
//                int bx = bxy.getKey();
//                int by = bxy.getValue();
//                graph[bx][by] = 'O';
//            }
//            for (int x = 0; x < R; x++) {
//                for (int y = 0; y < C; y++) {
//                    System.out.print(graph[x][y]);
//                }
//                System.out.println();
//            }
//
//        }
//
//    }
//}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        char[][] graph = new char[R][C];
        boolean[][] isBomb = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            graph[i] = br.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                if (graph[i][j] == 'O') {
                    isBomb[i][j] = true;
                }
            }
        }

        if (N == 1) {
            printGraph(graph);
        } else if (N % 2 == 0) {
            printAllBombs(R, C);
        } else {
            detonateBombs(R, C, graph, isBomb, N);
        }
    }

    private static void printGraph(char[][] graph) {
        for (char[] row : graph) {
            System.out.println(new String(row));
        }
    }

    private static void printAllBombs(int R, int C) {
        for (int i = 0; i < R; i++) {
            char[] row = new char[C];
            Arrays.fill(row, 'O');
            System.out.println(new String(row));
        }
    }

    private static void detonateBombs(int R, int C, char[][] graph, boolean[][] isBomb, int N) {
        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

        N /= 2;
        while (N-- > 0) {
            boolean[][] detonated = new boolean[R][C];
            for (int x = 0; x < R; x++) {
                for (int y = 0; y < C; y++) {
                    if (isBomb[x][y]) {
                        detonated[x][y] = true;
                        for (int[] dir : directions) {
                            int nx = x + dir[0];
                            int ny = y + dir[1];
                            if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                                detonated[nx][ny] = true;
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < R; i++) {
                Arrays.fill(isBomb[i], true);
            }
            for (int x = 0; x < R; x++) {
                for (int y = 0; y < C; y++) {
                    if (detonated[x][y]) {
                        isBomb[x][y] = false;
                    }
                }
            }
        }

        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                graph[x][y] = (isBomb[x][y]) ? 'O' : '.';
            }
        }
        printGraph(graph);
    }
}
