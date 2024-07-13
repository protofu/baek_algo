class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int len = numbers.length;
        int cnt = 1, d = 1;
        while (d != k+1) {
            if (cnt > len){
                cnt %= (len);
            }
            answer = cnt;               
            d++;
            cnt +=2;
        }
        
        return answer;
    }
}