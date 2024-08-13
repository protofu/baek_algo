import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int x1 = 0, y1 = 0, sum1 = 0, x2 = 0, y2 = 0, sum2 = 0, n = 2;
		x1 += Integer.parseInt(st.nextToken());
		y1 += Integer.parseInt(st.nextToken());
		sum1 += Integer.parseInt(st.nextToken());			
		x2 += Integer.parseInt(st.nextToken());
		y2 += Integer.parseInt(st.nextToken());
		sum2 += Integer.parseInt(st.nextToken());						
		for(int i=-999; i<=999; i++) {
			for(int j=-999; j<=999; j++) {
				if (x1*i + y1*j == sum1 && x2*i + y2*j == sum2) {
					System.out.println(i + " " + j);
					return;
				}
			}
		}
	}
}