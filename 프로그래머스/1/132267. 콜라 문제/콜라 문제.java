class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        return cola(a, b, n, answer);
    }
    // a -> 줘야하는, b-> 주면 받는, c -> 가지고 있는
    public int cola(int a, int b, int n, int answer){
        // 남은 병이 a보다 작으면 재귀 종료
        if (n < a) return answer;    
        // 아니라면 n <- 가지고 있는 병 수 계산 ||  answer <- 바꿔먹은 병 더하기
        return cola(a, b, n/a*b + n%a, answer + n/a*b);
    }
}