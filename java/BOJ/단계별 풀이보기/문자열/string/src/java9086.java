import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class java9086 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        sc.nextLine(); // 남은 개행 문자 소비

        for (int i = 0; i < m; i++) {
            String[] str = sc.nextLine().strip().split("");
            String s = str[0] + str[str.length - 1];
            System.out.println(s);
        }

//        for(String ss : arr){
//            System.out.println(ss);
//        }


    }
}
