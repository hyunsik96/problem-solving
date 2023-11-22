import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static char[] mo = {'a', 'e', 'i', 'o', 'u'};

    private static boolean checkMo(char c) {
        for (char m : mo) {
            if (m == c) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String word = br.readLine();
            if (word.equals("end")) {
                break;
            }

            boolean check = false;
            for (int i = 0; i < word.length(); i++) {

                boolean minusZero = checkMo(word.charAt(i));
                if (minusZero) {
                    check = true;
                }
                if (0 < i) {
                    if (word.charAt(i - 1) == word.charAt(i) && word.charAt(i) != 'e' && word.charAt(i) != 'o') {
                        check = false;
                        break;
                    }
                }
                if (1 < i) {
                    boolean minusOne = checkMo(word.charAt(i - 1));
                    boolean minusTwo = checkMo(word.charAt(i - 2));
                    if (minusTwo && minusOne && minusZero) {
                        check = false;
                        break;
                    }
                    if (!minusTwo && !minusOne && !minusZero) {
                        check = false;
                        break;
                    }
                }
            }
            if (check) {
                System.out.printf("<%s> is acceptable.\n", word);
            } else {
                System.out.printf("<%s> is not acceptable.\n", word);
            }
        }
    }
}

