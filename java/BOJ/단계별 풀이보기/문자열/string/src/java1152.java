import java.util.Arrays;
import java.util.Scanner;

public class java1152 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] st = sc.nextLine().strip().split(" ");
        int sum =0;
        for (String s : st){
            if (s.isEmpty()){
                continue;
            }
            sum+=1;
        }


        System.out.println(sum);
    }
}
