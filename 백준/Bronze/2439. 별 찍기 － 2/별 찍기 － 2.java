import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			String ans = "";
			for (int j = 0; j < n; j++) {
				if (j > (n-2) - i) {
					ans += "*";
				} else {
					ans += " ";
				}

			}
			System.out.println(ans);
		}
	}
}