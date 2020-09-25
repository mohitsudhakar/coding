// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

// import java.util.List;
import java.util.*;

import java.util.stream.Collectors;

class Solution {


    public static String solution(String S) {
        // write your code in Java SE 8


        // split by \n
        // split by comma
        // remove row if NULL in row


        List<String> rows = new ArrayList<>();

        String[] splittedRows = S.split("\n");
        List<String> strings = Arrays.asList(splittedRows);

        for (String string: strings) {
            String[] cells = string.split(",");
            List<String> cellList = Arrays.asList(cells);

            if (!cellList.contains("NULL")) {
                String res = cellList.stream().collect(Collectors.joining(","));
                rows.add(res);
            }

        }

        String ans = rows.stream().collect(Collectors.joining("\n"));
        return ans;

    }

    public static void main(String[] args) {
        String ans = solution("c,p,a\nuk,2m,2km2\nNULL,2,3");
        System.out.println(ans);
    }
}