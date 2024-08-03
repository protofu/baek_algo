import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int t = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer> canHomeRun = new ArrayList<>();
		// 세자리 다 다르면서, 0을 제외한 경우 후보에 넣음
		for (int i = 123; i <= 987; i++) {
			if (isDuplicated(String.valueOf(i))) continue;
			canHomeRun.add(i);
		}

		for(int i=0; i<t; i++) {
			st = new StringTokenizer(br.readLine());
			String num = st.nextToken();
			int s = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			// 순회하며 지울건데 어떻게 해야할까 생각하다 그냥 이터레이터 ㄱㄱ
			Iterator<Integer> iterator = canHomeRun.iterator();
			// 다음 요소가 있으면
			while (iterator.hasNext()) {
				// 스트라이크 볼이 맞지 않다면
				if(!isRight(num, String.valueOf(iterator.next()), s, b)) {
					// 반환한 마지막 요소 지우기
					iterator.remove();
				}
			}
		}
		System.out.println(canHomeRun.size());
		
	}
	// 중복 비교
	public static boolean isDuplicated(String num) {
		for (int i = 0; i < 2; i++) {
			for (int j = i+1; j < 3; j++) {
				if (num.charAt(i) == num.charAt(j) || num.contains("0")) return true;
			}
		}
		return false;
	}
	
	// 스트라이크 볼 비교
	public static boolean isRight(String num1, String num2, int s, int b) {
		int sCnt = 0, bCnt = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				// 스트라이크 인 경우
				if (i == j && num1.charAt(i) == num2.charAt(j)) {
					sCnt++;
				} else if(num1.charAt(i) == num2.charAt(j)) {
				// 볼인 경우
					bCnt++;
				}
			}
		}
		return s == sCnt && b == bCnt;
	}
}