import java.util.Arrays;
import java.util.Scanner;

public class java10988 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        String[] s = sc.nextLine().split("");
        int _max = s.length - 1;
        int ans = 1;
        for (int i = 0; i <  s.length /2 ; i++) {
            if (!s[i].equals(s[_max-i])){
                ans = 0;
                break;
            }
        }


        System.out.println(ans);

        sc.close();
    }
}
