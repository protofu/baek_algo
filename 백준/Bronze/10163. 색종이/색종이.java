import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int[][] paper = new int[1001][1001];
		int[][] range = new int[n][4];
		
		for (int i = 1; i < n+1; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			
			range[i-1] = new int[]{y, x, w, h};
			
			for (int j = y; j < y+h; j++) {
				for (int k = x; k < x+w; k++) {
					paper[j][k] = i;
				}
			}
			
		}
		for (int i = 1; i < n+1; i++) {
			int count = 0;
			for (int j = 0; j < 1001; j++) {
				for (int k = 0; k < 1001; k++) {
					if (paper[j][k] == i) {
						count += 1;
					};
				}
			}			
			System.out.println(count);
		}
		
	
	}
}