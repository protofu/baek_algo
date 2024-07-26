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
		StringTokenizer st;
		while(t-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			String cmd = st.nextToken();
			switch (cmd) {
			//push_front X: 정수 X를 덱의 앞에 넣는다.
			case "push_front":
				int f = Integer.parseInt(st.nextToken());
				q.addFirst(f);
				break;
			//push_back X: 정수 X를 덱의 뒤에 넣는다.
			case "push_back":
				int b = Integer.parseInt(st.nextToken());
				q.add(b);
				break;
			//pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
			//만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			case "pop_front":
				if (q.isEmpty()) {
					bw.write(-1 + "\n");
				}else {					
					bw.write(q.poll() + "\n");				
				}
				break;
			//pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
			//만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			case "pop_back":
				if (q.isEmpty()) {
					bw.write(-1 + "\n");
				}else {					
					bw.write(q.pollLast() + "\n");				
				}
				break;
			//size: 덱에 들어있는 정수의 개수를 출력한다.
			case "size":
				bw.write(q.size() + "\n");
				break;
			//empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
			case "empty":
				if (q.isEmpty())
					bw.write(1 + "\n");
				else
					bw.write(0 + "\n");
				break;
			//front: 덱의 가장 앞에 있는 정수를 출력한다. 
			//만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			case "front":
				if (q.isEmpty())
					bw.write(-1 + "\n");
				else
					bw.write(q.peek() + "\n");
				break;
			//back: 덱의 가장 뒤에 있는 정수를 출력한다. 
			//만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			case "back":
				if (q.isEmpty())
					bw.write(-1 + "\n");
				else
					bw.write(q.peekLast() + "\n");
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
