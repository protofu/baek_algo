import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String numStr = sc.nextLine();
        // 숫자를 배열로 저장하기 위한 배열 생성
        int[] num = new int[numStr.length()];
        // 각 인트로 넣어주기
        for (int i = 0; i < numStr.length(); i++) {
			num[i] = numStr.charAt(i)-48;
        }
        // 내림차순
        for (int i = 0; i < num.length-1; i++) {
			for (int j = 1; j < num.length; j++) {
				if (num[j] > num[j-1]) {
					int tmp = num[j];
					num[j] = num[j-1];
					num[j-1] = tmp;
				}
			}
		}
        
        for (int i : num) {
			System.out.print(i);
		}
    }
}