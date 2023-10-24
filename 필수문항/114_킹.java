import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {

    public static Character[] alpha = { ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' };
    public static String[] direction = { "R", "L", "B", "T", "RT", "LT", "RB", "LB" };
    public static int[][] xy = { { 1, 0 }, { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 1 }, { -1, 1 }, { 1, -1 }, { -1, -1 } };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String tmpKing = st.nextToken();
        String tmpStone = st.nextToken();
        int n = Integer.parseInt(st.nextToken());
        int[] king = { 0, 0 };
        int[] stone = { 0, 0 };
        king[0] = IntStream.range(1, 9).filter(i -> alpha[i] == tmpKing.charAt(0)).findFirst().orElse(-1);
        king[1] = Character.getNumericValue(tmpKing.charAt(1));
        stone[0] = IntStream.range(1, 9).filter(i -> alpha[i] == tmpStone.charAt(0)).findFirst().orElse(-1);
        stone[1] = Character.getNumericValue(tmpStone.charAt(1));

        while (n-- > 0) {
            String word = br.readLine();
            int[] tmp = xy[IntStream.range(0, 8).filter(i -> word.equals(direction[i])).findFirst().orElse(-1)];
            int kingX = king[0] + tmp[0];
            int kingY = king[1] + tmp[1];
            int stoneX = stone[0];
            int stoneY = stone[1];

            if (0 < kingX && kingX < 9 && 0 < kingY && kingY < 9) {
                if (kingX == stoneX && kingY == stoneY) {
                    if (0 < stoneX + tmp[0] && stoneX + tmp[0] < 9 && 0 < stoneY + tmp[1] && stoneY + tmp[1] < 9) {
                        king[0] = kingX;
                        king[1] = kingY;
                        stone[0] = stoneX + tmp[0];
                        stone[1] = stoneY + tmp[1];
                    }
                } else {
                    king[0] = kingX;
                    king[1] = kingY;
                }
            }
        }
        System.out.printf("%c%d\n", alpha[king[0]], king[1]);
        System.out.printf("%c%d", alpha[stone[0]], stone[1]);
    }
}