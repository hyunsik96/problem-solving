import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map.Entry;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int num = Integer.parseInt(br.readLine());
        int[] recs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int order = 1;
        Map<Integer, Integer[]> dic = new HashMap<>(); // key : number, value : [count, order]
        for (int r : recs) {
            if (dic.containsKey(r)) {
                dic.put(r, new Integer[] { dic.get(r)[0] + 1, dic.get(r)[1] });
            } else {
                if (dic.size() == N) {
                    List<Entry<Integer, Integer[]>> list = new ArrayList<>(dic.entrySet());
                    Collections.sort(list, new Comparator<Entry<Integer, Integer[]>>() {
                        public int compare(Entry<Integer, Integer[]> entry1, Entry<Integer, Integer[]> entry2) {
                            if (entry1.getValue()[0] < entry2.getValue()[0]) {
                                return -1;
                            } else if (entry1.getValue()[0] > entry2.getValue()[0]) {
                                return 1;
                            } else if (entry1.getValue()[1] < entry2.getValue()[1]) {
                                return -1;
                            } else {
                                return 1;
                            }
                        }
                    });
                    dic.remove(list.get(0).getKey());
                }
                dic.put(r, new Integer[] { 1, order++ });
            }
        }
        Integer[] a = dic.keySet().toArray(new Integer[0]);
        Arrays.sort(a);
        StringBuilder sb = new StringBuilder();
        for (Integer key : a) {
            sb.append(key);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb);
    }
}
