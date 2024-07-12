import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int ans = 3;
		if (x>0 && y>0) {
			ans = 1;
		} else if (x>0 && y<0) {
			ans = 4;
		} else if (x<0 && y>0) {
			ans = 2;
		}
		System.out.println(ans);
	}
}
