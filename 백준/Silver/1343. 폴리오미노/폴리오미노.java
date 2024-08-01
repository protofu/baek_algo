import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// . 단위로 배열 받기
		// .xx를 추가한 이유는 마지막 문자 뒤로 .이 여러개 붙을 수 있으니 그 경우 처리하려고
		String[] arr = (br.readLine()+".XX").split("\\.");
		// 덮을 수 있는지 없는지 체크하기위한 체크포인트 생성
		boolean isRight = true;
		// 결과 출력할 변수
		String tmp = "";
		// 입력이 . 만 있을 경우 예방
		if (arr.length == 0) {
			isRight = false;
		} else {			
			// 나눈 배열을 불러오며 조건에 맞춰 처리
			for (String s : arr) {
				int len = s.length();
				// 홀수라면 애초에 성립이 안되니까 체크포인트 바꿔주고 바로 깨기
				if (len%2 == 1) {
					isRight = false;
					break;
				} else {
					// 사전순으로 하는거라 A가 무조건 먼저 차도록 하기위해 4로 나눠지는지 먼저 확인
					if (len%4 == 0) {
						// 4로 나눠진 만큼 A 추가
						for (int i = 0; i < len; i++) {
							tmp += "A";
						}
					// 4보다 크다면 6 or 8 등등 있으므로
					} else if (len > 4) {
						// 먼저 4로나눈 몫 만큼 
						int cnt = len/4;
						// AAAA를 추가
						for (int i = 0; i < cnt; i++) {
							tmp += "AAAA";
						}
						// 나머지는 무조건 2일거니까 BB 추가
						tmp += "BB";
					// 위 조건이 다 아니면 무조건 길이가 2니까 BB 추가
					} else {
						tmp += "BB";
					}
					// 조건이 끝날때마다 -> 배열의 원소가 나눠졌단건 있던 .이 없어졌단 거니까
					// . 추가
					tmp+=".";
				}
			}
		}
		
		// 폴리오미노 가능하다면 출력 하는데 가장 뒤에도 . 이 붙으니까 그것 빼고 출력
		if (isRight) {	
			// 마지막 예외처리를 위한 문자열 넣은걸 빼주고 출력
			System.out.println(tmp.substring(0, tmp.length()-4));			
				
		} else {
			System.out.println(-1);
		}
	}
}