import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] S = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();

        boolean[] check = new boolean[(int) Math.pow(2, 20) + 1];
        int nowChecked = 0; // 현재 부분수열 합에 적용한 S 인덱스
        int maxNum = S[0]; // 현재 부분수열 합의 최대 숫자
        check[maxNum] = true;

        int checked = 0; // 현재 1부터 자연수 몇까지 확인했는지
        check[0] = true;

        int idx = 0;
        for (int num = 1; num < (int) Math.pow(2, 20) + 1; num++) {
            for (int i = idx; i < N; i++) {
                if (S[i] > num) {
                    idx = i;
                    break;
                }
            }
            if (idx != N && S[idx] <= num) {
                idx = N;
            }

            // idx 미만의 수로만 부분수열의 합 만들어야함
            if (idx - 1 > nowChecked) {
                int lap = idx - 1 - nowChecked;

                while (lap-- > 0) {
                    for (int i = 1; i <= maxNum; i++) {
                        if (check[i]) {
                            check[i + S[idx - 1]] = true;
                        }
                    }
                    check[S[idx - 1]] = true;
                    maxNum = maxNum + S[idx - 1];
                }

                nowChecked = idx - 1;
            }
            boolean ans = true;
            for (int i = checked; i <= num; i++) {
                if (!check[i]) {
                    ans = false;
                    break;
                }
            }
            if (ans) {
                checked = num;
            } else {
                System.out.println(num);
                return;
            }
        }
    }
}
