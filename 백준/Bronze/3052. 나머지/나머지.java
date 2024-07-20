import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[42];
		int num, ans = 0;
		for(int i=0; i<10; i++)	{
			num = sc.nextInt()%42;
			arr[num]++;
		}
		for (int i : arr) {
			if (i > 0) {
				ans++;
			}
		}
		System.out.println(ans);
	}
}