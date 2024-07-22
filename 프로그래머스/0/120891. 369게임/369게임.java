class Solution {
    public int solution(int order) {
        int answer = 0;
        int tmp = 0;
        // 자리수를 구해서 반복문 하긴 귀찮으니 while
        // order가 0 이 되면 끝내면 되니까 조건 설정
        while (order != 0) {
            // 한자리씩 비교
            tmp = order % 10;
            // 0이 아니면서 3으로 나눠지면 answer++
            if (tmp != 0 && tmp % 3 == 0){
                answer++;
            }
            // 그 다음 자리수를 보기위해 전처리
            order /= 10;
        }
        
        return answer;
    }
}
