import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		int maxNum = 0, num = 0;
		double sum = 0;
		String[] st = sc.nextLine().split(" ");

		for (int i=0;i<n;i++) {
			num = Integer.parseInt(st[i]);
			if (maxNum < num) maxNum = num;
		}
		for (int i=0;i<n;i++) {
			num = Integer.parseInt(st[i]);
			sum += (double) num*100/maxNum;
		}
		System.out.println(sum / n);
	}
}