import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] time = sc.nextLine().split(" ");
		int hour = Integer.parseInt(time[0]), minute = Integer.parseInt(time[1]);
		int needTime = sc.nextInt();
		
		minute += needTime;
		if (minute >= 60) {
			hour += minute / 60;
			minute %= 60;
		}
		if (hour >= 24) {
			hour -= 24;
		}
		System.out.println(hour + " " + minute);
		
		
	}
}