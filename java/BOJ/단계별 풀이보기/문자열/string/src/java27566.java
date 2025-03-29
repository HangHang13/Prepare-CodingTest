import java.util.Scanner;


public class java27566 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split("");

        System.out.println(str[sc.nextInt()-1]);
        sc.close();
    }
}
