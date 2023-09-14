import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int pack = 1001;
        int solo = 1001;
        for (int i = 0; i < m; i++) {
            StringTokenizer tmp = new StringTokenizer(br.readLine());
            int tmpPack = Integer.parseInt(tmp.nextToken());
            int tmpSolo = Integer.parseInt(tmp.nextToken());
            if (tmpPack < pack) {
                pack = tmpPack;
            }
            if (tmpSolo < solo) {
                solo = tmpSolo;
            }
        }
        if (6 * solo < pack) {
            pack = 6 * solo;
        }
        int quotient = n / 6;
        System.out.println((quotient * pack) + ((n - quotient * 6) * solo < pack ? (n - quotient * 6) * solo : pack));
    }
}