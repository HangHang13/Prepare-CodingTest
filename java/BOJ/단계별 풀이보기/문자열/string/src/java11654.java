import java.util.Scanner;

public class java11654 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ch = sc.nextLine();
        char[] charConvert = ch.toCharArray();
        for (char s : charConvert){
            System.out.println((int) s);
        }

    }
}
