import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] smalls = new int[9];
		int tmp  = 0;
		
		for (int i = 0; i < 9; i++) {
			smalls[i] = sc.nextInt();
			tmp += smalls[i];
		}
		for (int i = 0; i < 8; i++) {
			for (int j = i; j < 9; j++) {
				if(smalls[i]>smalls[j]) {
					int temp = smalls[i];
					smalls[i] = smalls[j];
					smalls[j] = temp;
				}
			}
		}
		boolean isDone = false;
		for (int i = 0; i < 9; i++) {
			for (int j = i; j < 9; j++) {
				if(tmp-smalls[i]-smalls[j] == 100) {
					smalls[i] = -1;
					smalls[j] = -1;
					isDone = true;
					break;
				}
			}
			if (isDone) {
				break;
			}
		}

		for (int i : smalls) {
			if (i > 0) {
				System.out.println(i);
			}
		}
	}

}
