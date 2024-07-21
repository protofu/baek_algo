import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt()+1;
		int m = sc.nextInt();
		int a, b;
		int[] arr = new int[n]; 
		for (int i = 1; i < n; i++) {
			arr[i] = i;
		}
		for(int i=0;i<m;i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			int tmp = arr[a];
			arr[a] = arr[b];
			arr[b] = tmp;
		}
		for (int i = 1; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}