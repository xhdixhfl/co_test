class Solution {
    public double solution(int[] numbers) {
        double sum = 0;
        for(double n : numbers) {
            sum += n;
        }
        return sum/numbers.length;
    }
}