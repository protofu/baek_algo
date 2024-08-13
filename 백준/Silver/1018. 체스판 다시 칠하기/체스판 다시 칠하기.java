import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int col = Integer.parseInt(st.nextToken());
		int row = Integer.parseInt(st.nextToken());
		String[][] board = new String[col][row];
		// 체스판 배열화 하기
		for (int i = 0; i < col; i++) {
			char[] c = br.readLine().toCharArray();
			for (int j = 0; j < row; j++) {
				board[i][j] = String.valueOf(c[j]);
			}
		}
		
		int ans = 32;
		// 전체 체스판 탐색 but 8x8 조사니까 -7 부분까지만.
		for (int i = 0; i < col-7; i++) {
			for (int j = 0; j < row-7; j++) {
				int cnt1 = 0, cnt2 = 0;
				// 최소 색칠 체스판 탐색
				for (int k = i; k < i+8; k++) {
					for (int q = j; q < j+8; q++) {
						// 첫 부분에 따라 카운팅
						// 첫 부분이 W 인경우
						if ((k+q)%2==0 && !board[k][q].equals("W")) { // 첫 칸 기준
							cnt1++;
						} else if ((k+q)%2!=0 && !board[k][q].equals("B")) {
							cnt1++;
						}
						
						if ((k+q)%2==0 && !board[k][q].equals("B")) { // 첫 칸 기준
							cnt2++;
						} else if ((k+q)%2!=0 && !board[k][q].equals("W")) {
							cnt2++;
						}
					}
				}
				if (cnt1 > cnt2 & ans > cnt2) {
					ans = cnt2;
				} else if (cnt1 < cnt2 & ans > cnt1) {
					ans = cnt1;
				}
			}
		}
		System.out.println(ans);
	}
}
