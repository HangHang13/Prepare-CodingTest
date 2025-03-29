import java.util.Scanner;

public class java11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        sc.nextLine();
        int sum = 0;
//        for (int i = 0; i < a; i++) {
        String[] input = sc.nextLine().split("");
        for(String s : input){
           sum += Integer.parseInt(s);
        }
//        }
        System.out.println(sum);


    }
}
