import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] trucks = new int[n];
        for (int i = 0; i < n; i++) {
            trucks[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> lane = new ArrayList<>();
        int weight = 0; // 현재 다리 위 무게
        int now = -1; // 현재 배열에 들어간 트럭 인덱스

        for (int i = 0; i < Math.min(n, w); i++) {
            if (weight + trucks[i] <= L) {
                weight += trucks[i];
                lane.add(i);
                now = i;
            } else {
                break;
            }
        }

        while (lane.size() < w) {
            lane.add(-1);
        }

        if (now == n - 1) {
            System.out.println(w + now + 1);
        } else {
            weight = 0;
            int lp = 0;
            int rp = w - 1;

            for (int i = 0; i <= rp; i++) {
                if (lane.get(i) != -1) {
                    weight += trucks[lane.get(i)];
                }
            }

            for (int i = now + 1; i < n; i++) {
                while (true) {
                    if (lane.get(lp) == -1) {
                        if (trucks[i] + weight <= L) {
                            lane.add(i);
                            weight += trucks[i];
                            lp++;
                            rp++;
                            break;
                        } else {
                            lane.add(-1);
                            lp++;
                            rp++;
                        }
                    } else {
                        if (weight - trucks[lane.get(lp)] + trucks[i] <= L) {
                            lane.add(i);
                            weight += -trucks[lane.get(lp)] + trucks[i];
                            lp++;
                            rp++;
                            break;
                        } else {
                            lane.add(-1);
                            weight -= trucks[lane.get(lp)];
                            lp++;
                            rp++;
                        }
                    }
                }
            }
            System.out.println(lane.size() + w);
        }
    }
}
