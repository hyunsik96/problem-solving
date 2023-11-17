import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private static int gcdArray(int[] numbers) {
        int gcd = gcd(numbers[0], numbers[1]);
        for (int i = 2; i < numbers.length; i++) {
            gcd = gcd(gcd, numbers[i]);
        }
        return gcd;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] trees = new int[n];
        int[] gap = new int[n - 1];
        trees[0] = Integer.parseInt(br.readLine());
        for (int i = 1; i < n; i++) {
            trees[i] = Integer.parseInt(br.readLine());
            gap[i - 1] = trees[i] - trees[i - 1];
        }
        int realGap = gcdArray(gap);
        System.out.println((trees[n - 1] - trees[0]) / realGap - n + 1);
    }
}
