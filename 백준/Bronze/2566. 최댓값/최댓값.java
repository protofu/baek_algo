import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int maxNum = 0, x = 1, y = 1;
	
		for (int i=0;i<9;i++) {
			for (int j=0;j<9;j++) {
				int n = sc.nextInt();
				if (maxNum < n) {
					maxNum = n;
					x = i+1;
					y = j+1;
				}
			}
		}
		System.out.println(maxNum);
		System.out.println(x+" "+y);

		sc.close();
	}
}