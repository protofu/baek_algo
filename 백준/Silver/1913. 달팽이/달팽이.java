import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        // 시간초과 이슈로 버퍼리더 라이터 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());

        // 배열을 그릴 공배열 생성
        int[][] nail = new int[n][n];
        int cnt = n * n, move = n;
        // 방향에 더하고 빼줄 상수이자 변수
        int d = 1;
        // 초기 위치
        int y = -1, x = 0;
        // 0이면 끝나게
        while (cnt != 0) {
            // 2번마다 이동 횟수가 바뀌니까 배열 2개를 두었습니다.
            for (int i = 0; i < move; i++) {
                // 좌표 이동
                y += d;
                nail[y][x] = cnt;
                cnt--;
            }
            // 이동횟수 빼기
            move--;
            // 위 for문과 동일
            for (int i = 0; i < move; i++) {
                x += d;
                nail[y][x] = cnt;
                cnt--;
            }
            // 방향의 결 자체가 달라짐
            d = -d;
        }
        // 타겟 위치를 기록
        int ty = 1, tx = 1;

        for (int col = 0; col < n; col++) {
            for (int row = 0; row < n; row++) {
                // 타겟 위치 찾기
                if (nail[col][row] == target) {
                    ty = col + 1;
                    tx = row + 1;
                }
                bw.write(nail[col][row] + " ");
            }
            bw.newLine();
        }
        bw.write(ty + " " + tx);
        bw.flush();
        bw.close();
    }
}
