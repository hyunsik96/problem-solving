import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x_a1 = Integer.parseInt(st.nextToken());
            int y_a1 = Integer.parseInt(st.nextToken());
            int x_a2 = Integer.parseInt(st.nextToken());
            int y_a2 = Integer.parseInt(st.nextToken());
            int x_b1 = Integer.parseInt(st.nextToken());
            int y_b1 = Integer.parseInt(st.nextToken());
            int x_b2 = Integer.parseInt(st.nextToken());
            int y_b2 = Integer.parseInt(st.nextToken());

            if ((!(x_a1 <= x_b1 && x_b1 <= x_a2) && !(x_a1 <= x_b2 && x_b2 <= x_a2))
                    && !(x_b1 <= x_a1 && x_a2 <= x_b2)
                    || (!(y_a1 <= y_b1 && y_b1 <= y_a2) && !(y_a1 <= y_b2 && y_b2 <= y_a2))
                            && !(y_b1 <= y_a1 && y_a2 <= y_b2)) {
                System.out.println("d");
            } else if ((!(x_a1 < x_b1 && x_b1 < x_a2) && !(x_a1 < x_b2 && x_b2 < x_a2))
                    && !(x_b1 <= x_a1 && x_a2 <= x_b2)
                    && (!(y_a1 < y_b1 && y_b1 < y_a2) && !(y_a1 < y_b2 && y_b2 < y_a2))
                    && !(y_b1 <= y_a1 && y_a2 <= y_b2)) {
                System.out.println("c");
            } else if ((!(x_a1 < x_b1 && x_b1 < x_a2) && !(x_a1 < x_b2 && x_b2 < x_a2))
                    && !(x_b1 <= x_a1 && x_a2 <= x_b2)
                    && !((!(y_a1 <= y_b1 && y_b1 <= y_a2) && !(y_a1 <= y_b2 && y_b2 <= y_a2))
                            && !(y_b1 <= y_a1 && y_a2 <= y_b2))
                    || !((!(x_a1 <= x_b1 && x_b1 <= x_a2) && !(x_a1 <= x_b2 && x_b2 <= x_a2))
                            && !(x_b1 <= x_a1 && x_a2 <= x_b2))
                            && ((!(y_a1 < y_b1 && y_b1 < y_a2) && !(y_a1 < y_b2 && y_b2 < y_a2))
                                    && !(y_b1 <= y_a1 && y_a2 <= y_b2))) {
                System.out.println("b");
            } else {
                System.out.println("a");
            }
        }
    }
}
