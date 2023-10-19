
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        PriorityQueue<Long> heapq = new PriorityQueue<>();
        long ans = 0;
        while(N-->0){
            long num = (long)Integer.parseInt(st.nextToken());
            heapq.offer(num);
            ans += num;
        }
        while(M-->0){
            long a = heapq.poll();
            long b = heapq.poll();
            ans += a+b;
            heapq.offer(a+b);
            heapq.offer(a+b);
        }
        System.out.println(ans);
    }
}
