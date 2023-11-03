import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine().trim();
        int L = S.length();

        if (L == 1) {
            System.out.println(1);
        } else if (L == 2) {
            if (S.charAt(0) == S.charAt(1)) {
                System.out.println(2);
            } else {
                System.out.println(3);
            }
        } else {
            for (int i = (L - 1) / 2; i < L - 1; i++) {
                if (L / 2 <= i) {
                    int lp = i - 1;
                    int rp = i + 1;
                    boolean check = false;
                    while (true) {
                        if (S.charAt(lp) == S.charAt(rp)) {
                            if (rp == L - 1) {
                                check = true;
                                break;
                            } else {
                                lp--;
                                rp++;
                            }
                        } else {
                            break;
                        }
                    }
                    if (check) {
                        System.out.println(i * 2 + 1);
                        return;
                    }
                }

                if (S.charAt(i) == S.charAt(i + 1)) {
                    if (i + 2 == L) {
                        System.out.println(i * 2 + 2);
                        return;
                    }
                    int lp = i - 1;
                    int rp = i + 2;
                    boolean check = false;
                    while (true) {
                        if (S.charAt(lp) == S.charAt(rp)) {
                            if (rp == L - 1) {
                                check = true;
                                break;
                            } else {
                                lp--;
                                rp++;
                            }
                        } else {
                            break;
                        }
                    }
                    if (check) {
                        System.out.println(i * 2 + 2);
                        return;
                    }
                }
            }
            System.out.println((L - 1) * 2 + 1);
        }
    }
}
