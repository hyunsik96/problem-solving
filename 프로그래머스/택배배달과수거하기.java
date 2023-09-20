class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        // 가장 멀리부터 배달, 가장멀리부터 수거
        long ans = 0;

        for (int i = n - 1; i >= 0; i--) {
            while (deliveries[i] > 0 || pickups[i] > 0) {
                ans += (i + 1) * 2;
                int delCap = cap;
                int pickCap = cap;

                int tmpI = i + 1;
                while (--tmpI >= 0) {
                    if (deliveries[tmpI] >= delCap) {
                        deliveries[tmpI] -= delCap;
                        break;
                    } else {
                        delCap -= deliveries[tmpI];
                        deliveries[tmpI] = 0;
                    }
                }

                tmpI = i + 1;
                while (--tmpI >= 0) {
                    if (pickups[tmpI] >= pickCap) {
                        pickups[tmpI] -= pickCap;
                        break;
                    } else {
                        pickCap -= pickups[tmpI];
                        pickups[tmpI] = 0;
                    }
                }

            }
        }
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(2, 7, new int[] { 1, 0, 2, 0, 1, 0, 2 }, new int[] { 0, 2, 0, 1, 0, 2, 0 }));
    }
}
