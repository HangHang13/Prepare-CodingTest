import java.util.*;
import java.util.stream.Collectors;

public class java1157 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        String[] s = sc.nextLine().split("");
//        String[] upperS = Arrays.stream(s).map(String::toUpperCase).toArray(String[]:: new);
//        Map<String, Long> frequent = Arrays.stream(upperS).collect(Collectors.groupingBy(c -> c, Collectors.counting()));
//        long _max = Collections.max(frequent.values());
//        List<String> maxKeys = frequent.entrySet().stream().filter(entry-> entry.getValue() == _max)
//                .map(Map.Entry::getKey)
//                .collect(Collectors.toList());
//
//        if (maxKeys.size()> 1){
//            System.out.println("?");
//        }else {
//            System.out.println(maxKeys.get(0));
//        }


        String input = sc.nextLine().toUpperCase();
        int[] count = new int[26];

        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(0);
            count[ch -'A']++;
        }

        int _max = -1;
        char res = '?';
        for (int i = 0; i < count.length; i++) {
            if (count[i] > _max){
                _max = count[i];
                res = (char) (i+'A');
            } else if (_max ==count[i]) {
                res = '?';
            }
        }

        System.out.println(res);

        sc.close();
    }
}
