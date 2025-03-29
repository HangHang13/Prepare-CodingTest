import java.util.Arrays;
import java.util.Scanner;

public class java10811 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str= sc.nextLine();
        String[] parts = str.split(" ");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);


        int [] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = i+1;
        }

        for (int k = 0; k < m; k++) {
            String strinput= sc.nextLine();
            String[] partsinput = strinput.split(" ");
            int i = Integer.parseInt(partsinput[0]);
            int j = Integer.parseInt(partsinput[1]);
            changeReverse(arr,i,j);

        }

        for (int i : arr){
            System.out.print(i+" ");
        }
        sc.close();
    }

    public static void changeReverse(int[] arr, int i,int j){
        int left = i -1;
        int right = j -1;

        while (left < right){
            int buffer;
            buffer=arr[left];
            arr[left] = arr[right];
            arr[right] = buffer;

            left++;
            right--;
        }
    }
}
