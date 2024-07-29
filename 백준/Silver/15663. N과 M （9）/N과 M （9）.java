import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static List<Integer> ans = new ArrayList<>();

	// 백트래킹 메서드 생성
	public static void back(int n, int m, int[] numList, boolean[] visited) throws IOException {
		// 재귀 종료 조건 및 답 도출
		if (ans.size() == m) {
			for (int i : ans) {
				bw.write(i + " ");
			}
			bw.newLine();
			return;
		}
		// 백트래킹 본격 구현
		int num = 0;
		for (int i = 0; i < n; i++) {
			// 방문은 당연하고, 이전 숫자와 같다면 당연히 겹치므로 넘기기
			if (visited[i] == true || num == numList[i]) continue;
			ans.add(numList[i]);
			// 숫자 저장해서 비교에 쓰기
			num = numList[i];
			visited[i] = true;
			back(n, m, numList, visited);
			ans.remove(ans.size()-1);
			visited[i] = false;
		}
	}
	public static void main(String[] args) throws IOException {		
		// 자연수 N과 M이 주어졌을 때, 
		// 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
		// 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		boolean[] visited = new boolean[n]; 
		int[] numList = new int[n];
		for (int i = 0; i < numList.length; i++) {
			numList[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(numList);
		br.close();
		back(n, m, numList, visited);
		bw.flush();
		bw.close();
	}
}