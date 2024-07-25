import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int t = Integer.parseInt(st.nextToken());
		// 도화지 만들고
		int[][] paper = new int[100][100];
		// 받은 인풋을 좌표로 생각해서 도화지에 채워주기
		while (t-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			int y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			
			for (int i = y; i < y+10; i++) {
				for (int j = x; j < x+10; j++) {
					paper[i][j] = 1;
				}
			}
		}
		// 순회하며 채워진 면적 구하기
		int size = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (paper[i][j] == 1) {
					size+=1;
				}
			}
		}
		System.out.println(size);
	}
}