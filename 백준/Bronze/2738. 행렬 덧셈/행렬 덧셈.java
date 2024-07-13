import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[][] mtx = new int[n][m];
	
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				int x = sc.nextInt();
				mtx[i][j] = x;
			}
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				int x = sc.nextInt();
				mtx[i][j] += x;
				System.out.print(mtx[i][j]+" ");
			}
			System.out.println();
		}
		sc.close();
	}
}