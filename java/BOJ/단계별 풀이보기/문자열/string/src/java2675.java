import java.util.Arrays;
import java.util.Scanner;

public class java2675 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String[] stringArr = sc.nextLine().split(" ");

            int cnt = Integer.parseInt(stringArr[0]);
            String str = stringArr[1];
            String[] strArr = str.split("");
            String answer = "";
            for (String st : strArr){
                for (int j = 0; j < cnt; j++) {
                    answer += st;
                }
            }
            System.out.println(answer);
        }
    }
}
