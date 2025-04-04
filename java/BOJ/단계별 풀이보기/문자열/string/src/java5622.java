import java.util.Arrays;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class java5622 {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, Set<String>> immutableMap = Map.of(
        1, Set.of("A", "B","C"),  // Set.of()도 불변 컬렉션
            2, Set.of("A", "B","C"),
                3, Set.of("D", "E", "F"),
                4, Set.of("D", "E", "F"),
                5, Set.of("D", "E", "F"),
                6, Set.of("D", "E", "F"),
                7, Set.of("D", "E", "F"),
                8, Set.of("D", "E", "F"),
                9, Set.of("D", "E", "F")
        );

        String [] arr = new String[8];

        arr[0] = "ABC";
        arr[1] = "DEF";
        arr[2] = "GHI";
        arr[3] = "JKL";
        arr[4] = "MNO";
        arr[5] = "PQRS";
        arr[6] = "TUV";
        arr[7] = "WXYZ";

        String [] s = sc.nextLine().split("");
        int sum = 0;
        for (String ss : s){
            for (int i = 0; i < arr.length; i++) {
                try {
                    if (arr[i].contains(ss)){
                        sum = sum +3 + i;
                    }
                }catch (Exception e){
                    continue;
                }

            }
        }

        System.out.println(sum);
    }
}
