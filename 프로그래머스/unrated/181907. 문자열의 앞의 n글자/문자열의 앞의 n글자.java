class Solution {
    public String solution(String my_string, int n) {
        char[] chAns = new char[n];
        my_string.getChars(0,n, chAns, 0);
        String subStr = String.valueOf(chAns);
        return subStr;
    }
}