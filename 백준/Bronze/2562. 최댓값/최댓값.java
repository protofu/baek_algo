import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int maxNum = 0, idx = 0;
		for (int i=1;i<=9;i++) {
			int n = sc.nextInt();
			if (maxNum < n) {
				maxNum = n;
				idx = i;
			}
		}
		System.out.println(maxNum);
		System.out.println(idx);
	}
}