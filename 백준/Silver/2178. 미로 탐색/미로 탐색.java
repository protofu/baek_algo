import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[][] maze = new int[n][m];
		
		// 미로 그리기
		for (int i = 0; i < n; i++) {
			String str = br.readLine();
			for (int j = 0; j < m; j++) {
				maze[i][j] = str.charAt(j)-'0';
			}
		}
		// 방문 찍기					
		Set<List<Integer>> visit = new HashSet<>();
		Queue<List<Integer>> q = new LinkedList<>();
		
		// bfs
		int y = 0, x = 0;
		visit.add(Arrays.asList(y, x));
		q.add(Arrays.asList(y, x, 1));
		int[][] d = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
				
		// 이하 bfs
		while (!q.isEmpty()) {
			List<Integer> abc = q.poll();
			if (abc.get(0) == n-1 && abc.get(1) == m-1) {
				System.out.println(abc.get(2));
				break;
			}
			for (int[] dyx : d) {
				int ny = abc.get(0) + dyx[0];
				int nx = abc.get(1) + dyx[1];
				int cnt = abc.get(2);
				List<Integer> posi = Arrays.asList(ny, nx);
				if (
						0<=ny && ny < n && 0 <= nx && nx < m && // 범위 췤
						!visit.contains(posi) && // 방문 췤
						maze[ny][nx] == 1 // 길 췤
				) {
					List<Integer> next = Arrays.asList(ny, nx, cnt+1);
					visit.add(posi);
					q.add(next);
				}
			}

		}
		
	}
}