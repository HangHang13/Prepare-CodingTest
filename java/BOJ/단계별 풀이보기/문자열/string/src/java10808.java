import java.util.Arrays;
import java.util.Scanner;

public class java10808 {
    public static void main(String[] args) {
        char[] alpha = new char[26];

        for (int i = 0; i < 26; i++) {
            alpha[i] = (char) ('a' +i);
        }

        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringBuilder combined = new StringBuilder();

        for (char ch : alpha){
            int i = str.indexOf(ch);
            combined.append(String.valueOf(i));
            combined.append(" ");
        }
        // 마지막 공백 제거
        if (combined.length() > 0) {
            combined.deleteCharAt(combined.length() - 1);
        }
        System.out.println(combined.toString());
    }
}