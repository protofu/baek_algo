import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// replace로 XXXX를 먼저 AAAA로 걸러주고 남은 XX를 B로 걸러준다
		String ans = br.readLine().replace("XXXX", "AAAA").replace("XX", "BB");
		// 만약 문자열에 X 가 남아있다면 -1
		if (ans.contains("X")) System.out.println(-1);
		// 아니면 그대로 출력
		else System.out.println(ans);
		
	}
}