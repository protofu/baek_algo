import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Stack<Integer> stack = new Stack<>();
		
		int cnt = Integer.parseInt(br.readLine());
		StringTokenizer st;
		while (cnt-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			String cmd = st.nextToken();
			switch (cmd) {
			case "push":
				int x = Integer.parseInt(st.nextToken());
				stack.add(x);
				break;
			case "pop":
				try {
					System.out.println(stack.pop());
				} catch (Exception e) {
					System.out.println(-1);
				}
				break;
			case "size":
				System.out.println(stack.size());
				break;
			case "empty":
				if (stack.isEmpty()) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
				break;
			case "top":
				if (stack.isEmpty()) {
					System.out.println(-1);
				} else {
					System.out.println(stack.peek());
				}
				break;
			}
		}
		br.close();
	}
}