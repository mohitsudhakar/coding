
class Solution {
    public static String solution(String S, int[] A) {
        // write your code in Java SE 8
        int curr = A[0];
        String ans = "" + S.charAt(0);

        while (curr != 0) {
            ans += S.charAt(curr);
            curr = A[curr];
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {5,2,0,1,6,4,8,3,7};
        String ans = solution("cdeenetpi", arr);
        System.out.println(ans);
    }
}
