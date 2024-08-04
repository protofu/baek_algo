class Solution {
    public int solution(int n) {
        return queen(0, n, new int[n]);
    }

    public int queen(int s, int n, int[] board) {
        if (s == n) return 1; // 모든 퀸이 배치된 경우

        int answer = 0;
        for (int i = 0; i < n; i++) {
            board[s] = i; // 현재 행 s에 퀸을 배치
            boolean isValid = true;
            for (int j = 0; j < s; j++) {
                // 같은 열이거나 대각선이 아닌지 검사
                if (board[j] == board[s] || Math.abs(board[s] - board[j]) == s - j) {
                    isValid = false;
                    break;
                }
            }

            if (isValid) {
                answer += queen(s + 1, n, board); // 다음 행으로 재귀 호출
            }
        }
        return answer;
    }
}
