import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int target = sc.nextInt();
		int selector = 0, beSelector = 0;;
		// 1부터 target까지
		for (int i = 1; i <= target; i++) {
			beSelector = i;
			selector = i;
			// 한자리씩 selector에 더해주고
			while (beSelector != 0) {
				int tmp = beSelector%10;
				selector += tmp;
				beSelector/=10;
			}
			// target과 같으면 반복 끝
			if (selector == target) {
				selector = i;
				break;
			} else {
				selector = 0;
			}
		}
		System.out.println(selector);
	}
}
