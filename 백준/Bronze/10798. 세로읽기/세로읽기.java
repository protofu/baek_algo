import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = new String[5];
        int maxLen = 0;
        // 문자열 받으면서 최대 길이 저장
        for (int i = 0; i < 5; i++) {
			arr[i] = sc.nextLine();
			if (arr[i].length() > maxLen) {
				maxLen = arr[i].length();
			}
        }
        // 최대길이보다 짧은 것들은 - 로 길이 채워주기
        for (int i = 0; i < arr.length; i++) {
        	if (arr[i].length() < maxLen) {
        		int cnt = maxLen - arr[i].length();
        		arr[i] += "-".repeat(cnt);
        	}
		}
        // 세로로 순회하면서 - 가 아닌것만 출력
        int idx = 0;
        for (int i = 0; i < maxLen; i++) {
			for (int j = 0; j < arr.length; j++) {
				if (arr[j].charAt(idx) != '-') {
					System.out.print(arr[j].charAt(idx));					
				}
			}
			idx++;
		}
        
    }
}