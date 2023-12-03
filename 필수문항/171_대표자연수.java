import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int binarySearch(int[] nums, int start, int end) {
        int mid = (start + end) / 2;
        int total = 0;
        int totalMinus = 0;
        int totalPlus = 0;
        for (int num : nums) {
            total += Math.abs(num - mid);
            totalMinus += Math.abs(num - mid + 1);
            totalPlus += Math.abs(num - mid - 1);
        }

        if (totalMinus <= total) {
            return binarySearch(nums, start, mid - 1);
        } else if (totalPlus < total) {
            return binarySearch(nums, mid + 1, end);
        } else {
            return mid;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums[0] = Integer.parseInt(st.nextToken());
        int min = nums[0];
        int max = nums[0];
        for (int i = 1; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            if (nums[i] < min) {
                min = nums[i];
            }
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        System.out.println(binarySearch(nums, min, max));
    }
}
