import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	// 숫자 체크할 가로세로 2차원 / 3x3 3차원 배열 생성
	static boolean[][] col = new boolean[9][10];
	static boolean[][] row = new boolean[9][10];
	static boolean[][][] box = new boolean[3][3][10];
	static boolean isFinish = false;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
	
		// 스도쿠 판 만들기
		int[][] sudoku = new int[9][9];
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				sudoku[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 0인 좌표를 담을 LinkedList 생성
		List<int[]> zeros = new LinkedList<>();
		int num = 0;
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				num = sudoku[i][j];
				// 0이라면 채워주기
				if (num == 0) {
					ArrayList<Integer> tmp = new ArrayList<>();
					zeros.add(new int[] {i, j});
				} else { // 0이 아니면 후보에서 제외
					col[j][num] = true;
					row[i][num] = true;
					box[i/3][j/3][num] = true;
				}
			}
		}
		solveSudoku(0, zeros, sudoku);
	}

	private static void solveSudoku(int fill, List<int[]> zeros, int[][] sudoku) {
		// 종료조건 스도쿠가 완성되면 출력
		if (fill == zeros.size()) {
			// flag를 세워서 연속탈출 가능하도록
			isFinish = true;
			for (int[] sud : sudoku) {
				for (int su : sud) {
					System.out.print(su + " ");
				}
				System.out.println();
			}
			return;
		}
		// nullPointError 방지
		if (zeros.isEmpty()) {
            return;
        }
		int[] coordinate = zeros.get(fill);
		int y = coordinate[0], x = coordinate[1];
		for (int i = 1; i < 10; i++) {
			if (!col[x][i] && !row[y][i] && !box[y/3][x/3][i]) {
				sudoku[y][x] = i;
				col[x][i] = true;
				row[y][i] = true;
				box[y/3][x/3][i] = true;
				solveSudoku(fill+1, zeros, sudoku);
				// flag를 세워서 연속탈출 가능하도록
				if (isFinish) return;
				col[x][i] = false;
				row[y][i] = false;
				box[y/3][x/3][i] = false;
				sudoku[y][x] = 0;
			}
		}
	}
}
