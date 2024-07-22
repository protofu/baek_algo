class Solution {
    public int[] solution(int[] answers) {
        // 수포자들 찍는 방식 하드코딩
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] thr = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        // 정답 갯수 기록해둘 배열
        int[] ans = {0, 0, 0};
        // 탐색
        for(int i=0;i<answers.length;i++){
            // 각 배열 길이별로 인덱스 초기화 하면서 탐색
            int i1 = i%5;
            int i2 = i%8;
            int i3 = i%10;
            if (answers[i] == one[i1]){
                ans[0]++;
            }
            if (answers[i] == two[i2]){
                ans[1]++;
            }
            if (answers[i] == thr[i3]){
                ans[2]++;
            }
        }
        int cnt = 0, idx=0;
        // 최대값 찾고
        int maxNum = 0;
	        for (int i : ans) {
				if (i > maxNum) {
					maxNum = i;
				}
			}
        // answer 배열 길이 정하려고 최대값 개수 측정
        for (int i = 0; i < 3; i++) {
            if (ans[i] == maxNum) {
                cnt++;
            }
        }
        // 배열 만들고
        int[] answer = new int[cnt];
        // 최대값인 애들 인덱스 맞춰 넣어주기
        for (int i=0;i<3;i++) {
            if (ans[i] == maxNum) {
                answer[idx] = i+1;
                idx++;
            }
        }        
        return answer;
    }
}