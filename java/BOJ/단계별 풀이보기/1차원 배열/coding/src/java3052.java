import java.util.HashSet;
import java.util.Scanner;

public class java3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> hashSet = new HashSet<>();

        for (int i=0; i<10;i++){
            int num = sc.nextInt();
            int divd = num % 42;
            hashSet.add(divd);
        }
        int ans = 0;
        for (int iter : hashSet){
            ans+=1;
        }
        System.out.println(ans);
    }
}
