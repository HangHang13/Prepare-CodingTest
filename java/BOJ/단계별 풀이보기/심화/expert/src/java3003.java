import java.util.Arrays;
import java.util.Scanner;

public class java3003 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] s = sc.nextLine().split(" ");
        int [] ss = Arrays.stream(s).mapToInt(Integer::parseInt).toArray();


        int[] chessPieces = {1, 1, 2, 2, 2, 8}; // 정답 배열
        for (int i = 0; i < ss.length; i++) {
            System.out.print(chessPieces[i] - ss[i] + " ");
        }
    }
}
