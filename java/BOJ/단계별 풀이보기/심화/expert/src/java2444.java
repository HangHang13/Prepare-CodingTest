import java.util.Scanner;

public class java2444 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int k = sc.nextInt();
        for (int i = 1; i <= k; i++) {

            for (int j = 1; j <= k -i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2*i -1; j++) {
                System.out.print("*");
            }



            System.out.println();
        }

        for (int i = k-1; i > 0 ; i--) {
            for (int j = 1; j <=k-i ; j++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= 2*i-1; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        
        sc.close();
    }
}
