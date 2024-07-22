class Solution {
    public int solution(int[][] board) {
        int boardSize = board.length;
        int answer = 0;
        // 8방향 탐색을 위해 dydx 선언
        int[][] dir = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
        // 안전한 지역을 확인하기위해 같은 크기의 0으로 채워진 2차원 배열 선언
        int[][] safeBoard = new int[boardSize][boardSize];
        // y, x 완전 탐색
        for(int y=0;y<boardSize;y++){
            for(int x=0;x<boardSize;x++){
                // 폭탄이 있다면
                if (board[y][x] == 1){
                    safeBoard[y][x] = 1;
                    // 8방향 탐색
                    for(int a=0;a<8;a++){
                        int ny = y + dir[a][0];
                        int nx = x + dir[a][1];
                        // 범위 벗어나면 continue
                        if (0>ny || boardSize<=ny || 0>nx || boardSize<=nx) continue;
                        // 위험지역 1 표시
                        safeBoard[ny][nx] = 1;
                    }
                }
            }
        }
        // 0인곳만 answer++
        for(int y=0;y<boardSize;y++){
            for(int x=0;x<boardSize;x++){
                if (safeBoard[y][x]==0){
                    answer++;
                }
            }
        }
        
        
        return answer;
    }
}
