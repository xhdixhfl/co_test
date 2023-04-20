class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if(Integer.parseInt(Integer.toString(a)+Integer.toString(b))>2*a*b) {
            answer = Integer.parseInt(Integer.toString(a)+Integer.toString(b));
        }else {
            answer=2*a*b;
        }
        return answer;
    }
}