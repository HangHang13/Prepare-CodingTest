import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Scanner;
import java.math.BigDecimal;
public class java1546 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        double[] arr = new double[n];

        BigDecimal[] bigArr = new BigDecimal[n];

        BigDecimal max = BigDecimal.ZERO;
        for (int i = 0; i < n; i++) {
            bigArr[i] = BigDecimal.valueOf(sc.nextInt());
            if (bigArr[i].compareTo(max)>0){
                max = bigArr[i];
            }
        }

        sc.close();

        BigDecimal hundred = new BigDecimal("100");
        BigDecimal sum = BigDecimal.ZERO;

        for (int i = 0; i < n; i++) {
            BigDecimal score = bigArr[i].divide(max,20,RoundingMode.HALF_UP).multiply(hundred);
            sum = sum.add(score);
        }

        BigDecimal avg = sum.divide(new BigDecimal(n),20, RoundingMode.HALF_UP);
        System.out.println(avg.stripTrailingZeros().toPlainString());
    }
}
