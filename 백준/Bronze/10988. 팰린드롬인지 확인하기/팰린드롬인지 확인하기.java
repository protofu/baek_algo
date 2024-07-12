import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] word = sc.nextLine().split("");
		int len = word.length;
		int ans = 1;
		for(int i=0; i<=len/2; i++) {
			if (word[i].equals(word[len-1-i]) == false) {
				ans = 0;
				break;
			}
		}
		System.out.println(ans);
	}
}