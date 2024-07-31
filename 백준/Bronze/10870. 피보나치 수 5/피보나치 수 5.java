import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println(fib(sc.nextInt()));
	}
	
	public static int fib(int n) {
		if (n == 1) return 1;
		else if (n==0) return 0;
		return fib(n-1)+fib(n-2);
	}
}