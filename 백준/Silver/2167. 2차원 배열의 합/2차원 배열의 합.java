import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		// 배열 생성
		int[][] arr = new int[n][m];
		// 배열 넣기
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine(), " ");
		// 횟수
		int t = Integer.parseInt(st.nextToken());
		// 좌표에 따른 배열합 구하기
		while(t-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			int sy = Integer.parseInt(st.nextToken());
			int sx = Integer.parseInt(st.nextToken());
			int ey = Integer.parseInt(st.nextToken());
			int ex = Integer.parseInt(st.nextToken());		
			int ans = 0;
			for (int i = sy-1; i < ey; i++) {
				for (int j = sx-1; j < ex; j++) {
					ans += arr[i][j];
				}
			}
			System.out.println(ans);
		}
		br.close();
	}
}