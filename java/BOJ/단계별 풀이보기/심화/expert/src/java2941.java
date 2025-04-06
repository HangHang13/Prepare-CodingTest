import java.util.Arrays;
import java.util.Scanner;

public class java2941 {
    public static void main(String[] args) {
        String[] alpha = {"c=","c-", "dz=","d-","lj","nj","s=","z="};
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String temp = s;
        int res = 0;
        for (String st : alpha){
            while (temp.contains(st)){
                res +=1;
                temp = temp.replaceFirst(st , " ");
            }
        }

        String[] temps = temp.split("");
        for (String tem : temps){
            if (!tem.equals(" ")){
                res+=1;
            }
        }

        sc.close();
        System.out.println(res);
    }
}
