import java.util.Scanner;

public class java5597 {
    public static void main(String[] args) {
        Boolean [] students = new Boolean[31];
        for (int i= 1; i<=30; i++){
            students[i]  = false;
        }
        Scanner sc = new Scanner(System.in);

        for (int i= 0; i<28; i++){
            int num = sc.nextInt();
            students[num]  = true;
        }

        for (int i =1; i<=30; i++){
            if (!students[i]){
                System.out.println(i);
            }else {continue;}
        }
    }
}
