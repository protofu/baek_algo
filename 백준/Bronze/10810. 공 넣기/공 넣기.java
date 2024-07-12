import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] iArr = sc.nextLine().split(" ");
		int n=Integer.parseInt(iArr[0]), m=Integer.parseInt(iArr[1]);
		int[] arr = new int[n+1];
		for (int i=0;i<m;i++) {
			String[] iArr2 = sc.nextLine().split(" ");
			int a=Integer.parseInt(iArr2[0]), b=Integer.parseInt(iArr2[1]), c=Integer.parseInt(iArr2[2]);
			for(int j=a;j<=b;j++) {
				arr[j] = c;
			}
		}
		for(int i=1;i<=n;i++) {
			System.out.println(arr[i]);
		}
		
	}
}