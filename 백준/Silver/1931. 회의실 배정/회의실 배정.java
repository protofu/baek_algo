import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int t = Integer.parseInt(st.nextToken());
		int[][] meetings = new int[t][2];
		// 미팅 시간 다 넣기
		for (int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			meetings[i][0] = Integer.parseInt(st.nextToken());
			meetings[i][1] = Integer.parseInt(st.nextToken());
		}
		
		br.close();
		// 배열 endtime 기준 정렬 같다면 start 기준
		Arrays.sort(meetings, (now, next) -> {
			if (now[1] == next[1]) {
				return Integer.compare(now[0], next[0]);
			}
			return Integer.compare(now[1], next[1]);	
		});
		// 지금 끝나는 시간과 다음 시작시간 비교해서 카운트
		int end = 0, ans = 0;
		for (int i = 0; i < t; i++) {
			if (end <= meetings[i][0]) {
				end = meetings[i][1];
				ans++;
			}
		}
		
		System.out.println(ans);
	}
}