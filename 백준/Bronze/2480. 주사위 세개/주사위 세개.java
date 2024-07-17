import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] ip = sc.nextLine().split(" ");
		// 인덱스 번호로 주사위 배열
		int[] dice = {0, 0, 0, 0, 0, 0, 0};
		// 인덱스 번호로 주사위 갯수 넣기
		for(String s : ip) {
			int diceNum = Integer.parseInt(s);
			dice[diceNum]++;
		}
		// 갯수 췤
		int cnt = 0, dN = 0;
		for (int i=1;i<=6;i++) {
			if (dice[i]>=2) {
				dN = i;
				cnt = dice[i];
			} else if (dice[i]>0 && cnt <= 1) {
				dN = i;
				cnt = 1;
			}
		}
		// 결과 뽑아내기
		int rw = 0;
		switch (cnt) {
			case 3: rw = 10000 + dN * 1000; break;
			case 2: rw =1000 + dN * 100; break;
			default: rw = dN * 100;
		};
		System.out.println(rw);
	}
}
