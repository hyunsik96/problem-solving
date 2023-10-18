import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<int[]> papers = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            papers.add(new int[] { i, Integer.parseInt(st.nextToken()) });
        }
        int now = 0;
        int size = N;
        while (true) {
            int[] tmp = papers.remove(now);
            size--;
            System.out.printf("%d ", tmp[0]);
            if (size == 0) {
                break;
            }
            int num = tmp[1];
            if (num > 0) {
                now = (now + num - 1) % size;
            } else {
                now = now + num;
                while (now < 0) {
                    now += size;
                }
            }
        }
    }
}