import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main{
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static List<Integer> ans = new ArrayList<>();
	static List<Integer> numList = new ArrayList<>();
	public static void back(int n, int m, int[] arr, int start) throws IOException {
		// 목표한 길이가 되면 출력하고 return으로 재귀 돌아가기
		if (ans.size() == m) {
			for (int i : ans) {
				bw.write(i + " ");
			}
			bw.newLine();
			return;
		}
		// 백트래킹 구현
		// start 포인트 넣기
		for (int i = start; i < arr.length; i++) {
			ans.add(arr[i]);
			back(n, m, arr, i);
			ans.remove(ans.size()-1);
		}
	}
	
	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		String[] ar =  br.readLine().split(" ");
		int[] arr = new int[ar.length];
		// String으로 받은 배열을 int로
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(ar[i]);
		}
		// 오름차순 정렬
		Arrays.sort(arr);
		back(n, m, arr, 0);
		br.close();
		bw.flush();
		bw.close();
	}
}