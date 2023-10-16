import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] nList = new int[N];
            for (int i = 0; i < N; i++) {
                nList[i] = Integer.parseInt(st.nextToken());
            }

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[][] mList = new int[M][2];
            for (int i = 0; i < M; i++) {
                mList[i][0] = Integer.parseInt(st.nextToken());
                mList[i][1] = i;
            }

            Arrays.sort(nList);
            Arrays.sort(mList, Comparator.comparingInt(arr -> arr[0]));
            int np = 0;
            int[] ansList = new int[M];

            for (int[] m : mList) {
                int mp = m[0];
                while (true) {
                    if (np >= N) {
                        ansList[m[1]] = 0;
                        break;
                    }
                    if (nList[np] == mp) {
                        ansList[m[1]] = 1;
                        np++;
                        break;
                    } else if (nList[np] > mp) {
                        ansList[m[1]] = 0;
                        break;
                    } else {
                        np++;
                    }
                }
            }
            for (int n : ansList) {
                System.out.println(n);
            }
        }
    }
}