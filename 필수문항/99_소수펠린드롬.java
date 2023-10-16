import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static boolean check(int num) {
        String word = Integer.toString(num);
        int lp = 0;
        int rp = word.length() - 1;
        while (lp <= rp) {
            if (word.charAt(lp) == word.charAt(rp)) {
                lp++;
                rp--;
            } else {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[] sosu = new boolean[1003002];
        sosu[0] = true;
        sosu[1] = true;
        for (int i = 2; i <= Math.sqrt(1003002); i++) {
            int num = i * i;
            while (num < 1003002) {
                sosu[num] = true;
                num += i;
            }
        }
        for (int i = N; i < 1003002; i++) {
            if (!sosu[i] && check(i)) {
                System.out.println(i);
                break;
            }
        }

    }

}