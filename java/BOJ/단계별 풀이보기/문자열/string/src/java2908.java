import java.util.Scanner;

public class java2908 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        // 숫자 뒤집기 함수 사용
        int first = reverseNum(input[0]);
        int second = reverseNum(input[1]);

        System.out.println(Math.max(first,second));

    }
    private static int reverseNum(String str){
        return Integer.parseInt(new StringBuilder(str).reverse().toString());
    }
}
