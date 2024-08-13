import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	static Map<Integer, List<Integer>> nodes;
	static int[] visit;
	static int cnt = 2;
	static List<Integer> ans = new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		nodes = new HashMap<>();
		visit = new int[n+1];
		// 노드 관계 정리
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			nodes.putIfAbsent(u, new ArrayList<>());
			nodes.get(u).add(v);
			nodes.putIfAbsent(v, new ArrayList<>());
			nodes.get(v).add(u);
		}
		// 오름차순
		for (List<Integer> list : nodes.values()) {
            Collections.sort(list);
        }
		visit[r] = 1;
		ans.add(r);
		dfs(r);
		
		for (int i = 1; i < n+1; i++) {
			System.out.println(visit[i]);
		}
	}
	public static void dfs(int start) {
		if (nodes.get(start) == null) return;
		for (Integer node : nodes.get(start)) {
			if (visit[node] == 0) {
				visit[node] = cnt++;
				ans.add(node);
				dfs(node);				
			}
		}
	}
}
