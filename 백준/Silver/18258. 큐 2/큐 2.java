import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		Deque<Integer> q = new LinkedList<>();
		int last = 0;
		StringTokenizer st;
		while(t-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			String cmd = st.nextToken();
			switch (cmd) {
			case "push":
				int x = Integer.parseInt(st.nextToken());
				q.add(x);
				last = x;
				break;
			case "pop":
				if (q.isEmpty()) {
					bw.write(-1 + "\n");
				}else {					
					bw.write(q.poll() + "\n");				
				}
				break;
			case "size":
				bw.write(q.size() + "\n");
				break;
			case "empty":
				if (q.isEmpty())
					bw.write(1 + "\n");
				else
					bw.write(0 + "\n");
				break;
			case "front":
				if (q.isEmpty())
					bw.write(-1 + "\n");
				else
					bw.write(q.peek() + "\n");
				break;
			case "back":
				if (q.isEmpty())
					bw.write(-1 + "\n");
				else
					bw.write(last + "\n");
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
