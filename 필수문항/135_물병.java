import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        int ans = 0;
        int now = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String num = Integer.toBinaryString(Integer.parseInt(st.nextToken()));
        List<Integer> N = new ArrayList<>();
        for (int i = num.length() - 1; i >= 0; i--) {
            int tmp = Character.getNumericValue(num.charAt(i));
            N.add(tmp);
            if (tmp == 1) {
                now++;
            }
        }

        int K = Integer.parseInt(st.nextToken());

        while (now > K) {
            for (int i = 0; i < N.size(); i++) {
                if (N.get(i) == 1) {
                    ans += Math.pow(2, i);
                    N.set(i, 0);
                    int tmp = i;
                    while (tmp < N.size() - 1 && N.get(tmp + 1) == 1) {
                        tmp++;
                        now--;
                        N.set(tmp, 0);
                    }
                    if (tmp == N.size() - 1) {
                        N.add(1);
                    } else {
                        N.set(tmp + 1, 1);
                    }
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}
