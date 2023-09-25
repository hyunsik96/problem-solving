import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        int[][] line = new int[6][2];
        int east = 0, west = 0, south = 0, north = 0;
        StringTokenizer st;
        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            line[i][0] = Integer.parseInt(st.nextToken());
            line[i][1] = Integer.parseInt(st.nextToken());
            switch (line[i][0]) {
                case 1:
                    east++;
                    break;
                case 2:
                    west++;
                    break;
                case 3:
                    south++;
                    break;
                case 4:
                    north++;
                    break;
            }
        }
        int row = east == 1 ? 1 : 2;
        int col = south == 1 ? 3 : 4;
        int idx = 0;
        int next = 0;
        for (int i = 0; i < 6; i++) {
            idx = i;
            next = (i + 1) % 6;
            if ((line[idx][0] == row || line[idx][0] == col) && (line[next][0] == row || line[next][0] == col)) {
                break;
            }
        }
        int big = line[idx][1] * line[next][1];
        int small = line[(next + 2) % 6][1] * line[(next + 3) % 6][1];
        System.out.println((big - small) * k);

    }
}

