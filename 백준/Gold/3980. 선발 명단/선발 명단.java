import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static int ans = 0;
	static boolean[] visited = new boolean[11];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
	
		int testCase = Integer.parseInt(st.nextToken());
		
		while(testCase-- > 0) {
			// 선수 현황판 작성
			int[][] players = new int[11][11];
			for (int i = 0; i < 11; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 11; j++) {
					players[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			// 정답 도출할 전역 변수 0으로 만들고
			ans = 0;
			// 백트래킹 시작
			backT(players, 0, 0);
			// 정답 도출
			System.out.println(ans);
		}
	}

	public static void backT(int[][] players, int posiScore, int posi) {
		// 백트래킹 종료조건 
		// posi가 11이면 지금까지의 가장 큰 점수와 현재 점수 비교해서 큰걸로 초기화
		if (posi == 11) {
			ans = Math.max(ans, posiScore);
			return;
		}
		for (int i = 0; i < 11; i++) {
			// 포지션 스코어가 0이거나 이미 더해준 선수면 패스
			 if (players[posi][i] == 0 || visited[i]) continue;
			 visited[i] = true;
			 // 포지션스코어를 총스코어에 더해주고, 다음 포지션으로 파라미터 업데이트하면서 재귀
			 backT(players, posiScore+players[posi][i], posi+1);
			 visited[i] = false;
		}
	}
}